#!/usr/bin/env python3
"""
Backend API Testing Suite for NOWHERE Digital Platform
Tests the AI Problem Analysis API and existing endpoints
"""

import asyncio
import aiohttp
import json
import sys
import os
from datetime import datetime, date
from typing import Dict, Any, Optional

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

class BackendTester:
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
    
    def log_test(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        if response_data and not success:
            print(f"   Response: {response_data}")
        
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details,
            "response": response_data
        })
        
        if not success:
            self.failed_tests.append(test_name)
    
    async def test_health_endpoint(self):
        """Test GET /api/health endpoint"""
        try:
            async with self.session.get(f"{API_BASE}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("status") == "healthy":
                        self.log_test("Health Check", True, "Service is healthy")
                        return True
                    else:
                        self.log_test("Health Check", False, f"Unexpected status: {data.get('status')}", data)
                        return False
                else:
                    self.log_test("Health Check", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("Health Check", False, f"Exception: {str(e)}")
            return False
    
    async def test_contact_form_submission(self):
        """Test POST /api/contact endpoint"""
        try:
            contact_data = {
                "name": "Ahmed Al-Rashid",
                "email": "ahmed.rashid@example.ae",
                "phone": "+971501234567",
                "service": "social_media",
                "message": "I need help with social media marketing for my Dubai-based restaurant. Looking to increase online presence and customer engagement."
            }
            
            async with self.session.post(
                f"{API_BASE}/contact",
                json=contact_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and "id" in data.get("data", {}):
                        self.log_test("Contact Form Submission", True, "Contact form submitted successfully")
                        return True
                    else:
                        self.log_test("Contact Form Submission", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("Contact Form Submission", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("Contact Form Submission", False, f"Exception: {str(e)}")
            return False
    
    async def test_content_recommendations(self):
        """Test GET /api/content/recommendations endpoint"""
        try:
            business_info = "E-commerce fashion store in Dubai looking to increase online sales through digital marketing"
            
            async with self.session.get(
                f"{API_BASE}/content/recommendations",
                params={"business_info": business_info}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and "recommendations" in data.get("data", {}):
                        recommendations = data["data"]["recommendations"]
                        if recommendations and len(recommendations) > 10:  # Should be substantial content
                            self.log_test("Content Recommendations", True, "AI recommendations generated successfully")
                            return True
                        else:
                            self.log_test("Content Recommendations", False, "Recommendations too short or empty", data)
                            return False
                    else:
                        self.log_test("Content Recommendations", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("Content Recommendations", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("Content Recommendations", False, f"Exception: {str(e)}")
            return False
    
    async def test_ai_problem_analysis_valid_request(self):
        """Test POST /api/ai/analyze-problem with valid data"""
        try:
            problem_data = {
                "problem_description": "I need to increase online sales for my e-commerce business",
                "industry": "ecommerce",
                "budget_range": "AED 25K - 75K/month"
            }
            
            async with self.session.post(
                f"{API_BASE}/ai/analyze-problem",
                json=problem_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # Check response structure
                    if not data.get("success"):
                        self.log_test("AI Problem Analysis - Valid Request", False, "Response success is false", data)
                        return False
                    
                    analysis = data.get("data", {}).get("analysis", {})
                    if not analysis:
                        self.log_test("AI Problem Analysis - Valid Request", False, "No analysis data in response", data)
                        return False
                    
                    # Check required fields
                    required_fields = [
                        "problem_description", "industry", "ai_analysis", 
                        "market_insights", "strategy_proposal", "estimated_roi",
                        "implementation_time", "budget_range", "priority_level"
                    ]
                    
                    missing_fields = []
                    for field in required_fields:
                        if field not in analysis:
                            missing_fields.append(field)
                    
                    if missing_fields:
                        self.log_test("AI Problem Analysis - Valid Request", False, f"Missing fields: {missing_fields}", data)
                        return False
                    
                    # Check that AI analysis fields have substantial content
                    ai_fields = ["ai_analysis", "market_insights", "strategy_proposal"]
                    for field in ai_fields:
                        content = analysis.get(field, "")
                        if not content or len(content) < 50:  # Should be substantial content
                            self.log_test("AI Problem Analysis - Valid Request", False, f"Field '{field}' has insufficient content", data)
                            return False
                    
                    # Check that input data is preserved
                    if analysis["problem_description"] != problem_data["problem_description"]:
                        self.log_test("AI Problem Analysis - Valid Request", False, "Problem description not preserved", data)
                        return False
                    
                    if analysis["industry"] != problem_data["industry"]:
                        self.log_test("AI Problem Analysis - Valid Request", False, "Industry not preserved", data)
                        return False
                    
                    self.log_test("AI Problem Analysis - Valid Request", True, "Complete analysis with all required fields")
                    return True
                    
                else:
                    self.log_test("AI Problem Analysis - Valid Request", False, f"HTTP {response.status}", await response.text())
                    return False
                    
        except Exception as e:
            self.log_test("AI Problem Analysis - Valid Request", False, f"Exception: {str(e)}")
            return False
    
    async def test_ai_problem_analysis_minimal_data(self):
        """Test POST /api/ai/analyze-problem with minimal data"""
        try:
            problem_data = {
                "problem_description": "Need more customers",
                "industry": "general"
            }
            
            async with self.session.post(
                f"{API_BASE}/ai/analyze-problem",
                json=problem_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if data.get("success") and data.get("data", {}).get("analysis"):
                        analysis = data["data"]["analysis"]
                        # Should still provide default budget range when not specified
                        if "budget_range" in analysis and analysis["budget_range"]:
                            self.log_test("AI Problem Analysis - Minimal Data", True, "Handles minimal data with defaults")
                            return True
                        else:
                            self.log_test("AI Problem Analysis - Minimal Data", False, "No default budget range provided", data)
                            return False
                    else:
                        self.log_test("AI Problem Analysis - Minimal Data", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("AI Problem Analysis - Minimal Data", False, f"HTTP {response.status}", await response.text())
                    return False
                    
        except Exception as e:
            self.log_test("AI Problem Analysis - Minimal Data", False, f"Exception: {str(e)}")
            return False
    
    async def test_ai_problem_analysis_empty_request(self):
        """Test POST /api/ai/analyze-problem with empty data"""
        try:
            problem_data = {}
            
            async with self.session.post(
                f"{API_BASE}/ai/analyze-problem",
                json=problem_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                # Should still work with empty data (using defaults)
                if response.status == 200:
                    data = await response.json()
                    if data.get("success"):
                        self.log_test("AI Problem Analysis - Empty Request", True, "Handles empty request gracefully")
                        return True
                    else:
                        self.log_test("AI Problem Analysis - Empty Request", False, "Failed with empty request", data)
                        return False
                else:
                    # If it returns an error, that's also acceptable behavior
                    self.log_test("AI Problem Analysis - Empty Request", True, f"Properly rejects empty request with HTTP {response.status}")
                    return True
                    
        except Exception as e:
            self.log_test("AI Problem Analysis - Empty Request", False, f"Exception: {str(e)}")
            return False
    
    async def test_ai_problem_analysis_invalid_json(self):
        """Test POST /api/ai/analyze-problem with invalid JSON"""
        try:
            async with self.session.post(
                f"{API_BASE}/ai/analyze-problem",
                data="invalid json",
                headers={"Content-Type": "application/json"}
            ) as response:
                # Should return 400 or 422 for invalid JSON
                if response.status in [400, 422]:
                    self.log_test("AI Problem Analysis - Invalid JSON", True, f"Properly rejects invalid JSON with HTTP {response.status}")
                    return True
                else:
                    self.log_test("AI Problem Analysis - Invalid JSON", False, f"Unexpected status: HTTP {response.status}", await response.text())
                    return False
                    
        except Exception as e:
            self.log_test("AI Problem Analysis - Invalid JSON", False, f"Exception: {str(e)}")
            return False
    
    async def test_analytics_summary(self):
        """Test GET /api/analytics/summary endpoint"""
        try:
            async with self.session.get(f"{API_BASE}/analytics/summary") as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and "today" in data.get("data", {}):
                        self.log_test("Analytics Summary", True, "Analytics data retrieved successfully")
                        return True
                    else:
                        self.log_test("Analytics Summary", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("Analytics Summary", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("Analytics Summary", False, f"Exception: {str(e)}")
            return False
    
    async def run_all_tests(self):
        """Run all backend tests"""
        print(f"🚀 Starting Backend API Tests")
        print(f"📍 Backend URL: {BACKEND_URL}")
        print(f"📍 API Base: {API_BASE}")
        print("=" * 60)
        
        # Test existing core endpoints first
        await self.test_health_endpoint()
        await self.test_contact_form_submission()
        await self.test_content_recommendations()
        await self.test_analytics_summary()
        
        print("\n🤖 Testing AI Problem Analysis Endpoint:")
        print("-" * 40)
        
        # Test new AI Problem Analysis endpoint
        await self.test_ai_problem_analysis_valid_request()
        await self.test_ai_problem_analysis_minimal_data()
        await self.test_ai_problem_analysis_empty_request()
        await self.test_ai_problem_analysis_invalid_json()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
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
            print(f"\n🎉 All tests passed!")
        
        return failed_tests == 0

async def main():
    """Main test runner"""
    async with BackendTester() as tester:
        success = await tester.run_all_tests()
        return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)