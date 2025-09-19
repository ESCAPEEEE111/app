#!/usr/bin/env python3
"""
Error Handling and Edge Cases Test Suite
Tests backend API error handling and edge cases
"""

import asyncio
import aiohttp
import json
import sys

# Get backend URL from frontend .env file
def get_backend_url():
    """Get backend URL from frontend .env file"""
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"Error reading frontend .env: {e}")
    return "http://localhost:8001"

BACKEND_URL = get_backend_url()
API_BASE = f"{BACKEND_URL}/api"

class ErrorHandlingTester:
    def __init__(self):
        self.session = None
        self.test_results = []
        self.failed_tests = []
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details
        })
        
        if not success:
            self.failed_tests.append(test_name)
    
    async def test_invalid_endpoints(self):
        """Test invalid endpoint handling"""
        try:
            async with self.session.get(f"{API_BASE}/nonexistent") as response:
                if response.status == 404:
                    self.log_test("Invalid Endpoint Handling", True, "Properly returns 404 for non-existent endpoints")
                    return True
                else:
                    self.log_test("Invalid Endpoint Handling", False, f"Unexpected status: {response.status}")
                    return False
        except Exception as e:
            self.log_test("Invalid Endpoint Handling", False, f"Exception: {str(e)}")
            return False
    
    async def test_malformed_contact_data(self):
        """Test contact form with malformed data"""
        try:
            # Missing required fields
            contact_data = {
                "name": "Test User"
                # Missing email, phone, service, message
            }
            
            async with self.session.post(
                f"{API_BASE}/contact",
                json=contact_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status in [400, 422]:  # Should return validation error
                    self.log_test("Malformed Contact Data", True, f"Properly validates contact data with HTTP {response.status}")
                    return True
                else:
                    self.log_test("Malformed Contact Data", False, f"Unexpected status: {response.status}")
                    return False
        except Exception as e:
            self.log_test("Malformed Contact Data", False, f"Exception: {str(e)}")
            return False
    
    async def test_invalid_chat_session(self):
        """Test chat message with invalid session ID"""
        try:
            message_data = {
                "session_id": "invalid-session-id-12345",
                "message": "Test message",
                "user_id": "test_user"
            }
            
            async with self.session.post(
                f"{API_BASE}/chat/message",
                json=message_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                # Should handle gracefully (either work or return appropriate error)
                if response.status in [200, 400, 404, 422]:
                    self.log_test("Invalid Chat Session", True, f"Handles invalid session ID appropriately with HTTP {response.status}")
                    return True
                else:
                    self.log_test("Invalid Chat Session", False, f"Unexpected status: {response.status}")
                    return False
        except Exception as e:
            self.log_test("Invalid Chat Session", False, f"Exception: {str(e)}")
            return False
    
    async def test_large_payload_handling(self):
        """Test handling of large payloads"""
        try:
            # Create a large problem description
            large_description = "This is a very long business problem description. " * 1000  # ~50KB
            
            problem_data = {
                "problem_description": large_description,
                "industry": "technology",
                "budget_range": "AED 10,000 - 20,000/month"
            }
            
            async with self.session.post(
                f"{API_BASE}/ai/analyze-problem",
                json=problem_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status in [200, 413, 422]:  # 200 = handled, 413 = payload too large, 422 = validation error
                    self.log_test("Large Payload Handling", True, f"Handles large payload appropriately with HTTP {response.status}")
                    return True
                else:
                    self.log_test("Large Payload Handling", False, f"Unexpected status: {response.status}")
                    return False
        except Exception as e:
            self.log_test("Large Payload Handling", False, f"Exception: {str(e)}")
            return False
    
    async def test_concurrent_requests(self):
        """Test handling of concurrent requests"""
        try:
            # Create multiple concurrent health check requests
            tasks = []
            for i in range(10):
                task = self.session.get(f"{API_BASE}/health")
                tasks.append(task)
            
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            success_count = 0
            for response in responses:
                if hasattr(response, 'status') and response.status == 200:
                    success_count += 1
                    await response.release()  # Clean up response
            
            if success_count >= 8:  # Allow for some failures due to rate limiting
                self.log_test("Concurrent Requests", True, f"Handled {success_count}/10 concurrent requests successfully")
                return True
            else:
                self.log_test("Concurrent Requests", False, f"Only {success_count}/10 requests succeeded")
                return False
                
        except Exception as e:
            self.log_test("Concurrent Requests", False, f"Exception: {str(e)}")
            return False
    
    async def test_content_type_validation(self):
        """Test content type validation"""
        try:
            # Send JSON data without proper content type
            async with self.session.post(
                f"{API_BASE}/contact",
                data='{"name": "Test User", "email": "test@example.com"}',
                headers={"Content-Type": "text/plain"}
            ) as response:
                if response.status in [400, 415, 422]:  # Should reject improper content type
                    self.log_test("Content Type Validation", True, f"Properly validates content type with HTTP {response.status}")
                    return True
                else:
                    self.log_test("Content Type Validation", False, f"Unexpected status: {response.status}")
                    return False
        except Exception as e:
            self.log_test("Content Type Validation", False, f"Exception: {str(e)}")
            return False
    
    async def run_error_tests(self):
        """Run all error handling tests"""
        print(f"🛡️ Starting Error Handling and Edge Cases Tests")
        print(f"📍 Backend URL: {BACKEND_URL}")
        print(f"📍 API Base: {API_BASE}")
        print("=" * 60)
        
        print("\n🔍 Testing Error Handling:")
        print("-" * 40)
        await self.test_invalid_endpoints()
        await self.test_malformed_contact_data()
        await self.test_invalid_chat_session()
        await self.test_large_payload_handling()
        await self.test_concurrent_requests()
        await self.test_content_type_validation()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 ERROR HANDLING TEST SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t["success"]])
        failed_tests = len(self.failed_tests)
        
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if self.failed_tests:
            print(f"\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"   - {test}")
        else:
            print(f"\n🎉 All error handling tests passed!")
        
        return failed_tests == 0

async def main():
    """Main test runner"""
    async with ErrorHandlingTester() as tester:
        success = await tester.run_error_tests()
        return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)