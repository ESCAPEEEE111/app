#!/usr/bin/env python3
"""
Dubai Business Specific Backend API Tests
Tests with realistic Dubai/UAE business scenarios
"""

import asyncio
import aiohttp
import json
import sys
import os
from datetime import datetime

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

class DubaiBusinessTester:
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
    
    def log_test(self, test_name: str, success: bool, details: str = "", response_data: any = None):
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
    
    async def test_dubai_restaurant_problem(self):
        """Test AI Problem Analysis for Dubai restaurant business"""
        try:
            problem_data = {
                "problem_description": "My traditional Emirati restaurant in Dubai Marina needs to attract more tourists and young professionals. We have authentic cuisine but low online visibility and foot traffic.",
                "industry": "hospitality",
                "budget_range": "AED 20,000 - 40,000/month"
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
                        
                        # Check that analysis contains relevant content
                        ai_analysis = analysis.get("ai_analysis", "").lower()
                        market_insights = analysis.get("market_insights", "").lower()
                        strategy_proposal = analysis.get("strategy_proposal", "").lower()
                        
                        # Verify the analysis addresses the specific problem
                        if len(ai_analysis) > 50 and len(market_insights) > 50 and len(strategy_proposal) > 50:
                            self.log_test("Dubai Restaurant Problem Analysis", True, "Comprehensive analysis provided for Dubai restaurant scenario")
                            return True
                        else:
                            self.log_test("Dubai Restaurant Problem Analysis", False, "Analysis content insufficient", data)
                            return False
                    else:
                        self.log_test("Dubai Restaurant Problem Analysis", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("Dubai Restaurant Problem Analysis", False, f"HTTP {response.status}", await response.text())
                    return False
                    
        except Exception as e:
            self.log_test("Dubai Restaurant Problem Analysis", False, f"Exception: {str(e)}")
            return False
    
    async def test_uae_ecommerce_problem(self):
        """Test AI Problem Analysis for UAE e-commerce business"""
        try:
            problem_data = {
                "problem_description": "Our online fashion boutique targeting UAE women needs to compete with international brands. We need better conversion rates and customer retention strategies.",
                "industry": "ecommerce",
                "budget_range": "AED 50,000 - 100,000/month"
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
                        
                        # Verify all required fields are present
                        required_fields = ["ai_analysis", "market_insights", "strategy_proposal", "estimated_roi", "implementation_time"]
                        missing_fields = [field for field in required_fields if not analysis.get(field)]
                        
                        if not missing_fields:
                            self.log_test("UAE E-commerce Problem Analysis", True, "Complete analysis for UAE e-commerce scenario")
                            return True
                        else:
                            self.log_test("UAE E-commerce Problem Analysis", False, f"Missing fields: {missing_fields}", data)
                            return False
                    else:
                        self.log_test("UAE E-commerce Problem Analysis", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("UAE E-commerce Problem Analysis", False, f"HTTP {response.status}", await response.text())
                    return False
                    
        except Exception as e:
            self.log_test("UAE E-commerce Problem Analysis", False, f"Exception: {str(e)}")
            return False
    
    async def test_dubai_contact_form_submission(self):
        """Test contact form with Dubai business data"""
        try:
            contact_data = {
                "name": "Fatima Al-Zahra",
                "email": "fatima.alzahra@dubaitech.ae",
                "phone": "+971504567890",
                "service": "content_marketing",
                "message": "We are a Dubai-based fintech startup looking for comprehensive digital marketing services to establish our brand in the UAE market. We need help with social media, content marketing, and lead generation strategies."
            }
            
            async with self.session.post(
                f"{API_BASE}/contact",
                json=contact_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and "id" in data.get("data", {}):
                        self.log_test("Dubai Contact Form Submission", True, "Dubai business contact form submitted successfully")
                        return True
                    else:
                        self.log_test("Dubai Contact Form Submission", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("Dubai Contact Form Submission", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("Dubai Contact Form Submission", False, f"Exception: {str(e)}")
            return False
    
    async def test_uae_business_recommendations(self):
        """Test content recommendations for UAE business"""
        try:
            business_info = "Luxury real estate agency in Dubai specializing in high-end properties for international investors, looking to enhance digital presence and attract HNW clients"
            
            async with self.session.get(
                f"{API_BASE}/content/recommendations",
                params={"business_info": business_info}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and "recommendations" in data.get("data", {}):
                        recommendations = data["data"]["recommendations"]
                        if recommendations and len(recommendations) > 50:  # Should be substantial content
                            self.log_test("UAE Business Recommendations", True, "AI recommendations generated for UAE luxury real estate")
                            return True
                        else:
                            self.log_test("UAE Business Recommendations", False, "Recommendations too short or empty", data)
                            return False
                    else:
                        self.log_test("UAE Business Recommendations", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("UAE Business Recommendations", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("UAE Business Recommendations", False, f"Exception: {str(e)}")
            return False
    
    async def test_dubai_chat_scenario(self):
        """Test chat system with Dubai business scenario"""
        try:
            # Create chat session
            async with self.session.post(
                f"{API_BASE}/chat/session",
                json={},
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status != 200:
                    self.log_test("Dubai Chat Scenario", False, f"Failed to create session: HTTP {response.status}")
                    return False
                
                session_data = await response.json()
                session_id = session_data["data"]["session_id"]
            
            # Send Dubai-specific message
            message_data = {
                "session_id": session_id,
                "message": "I run a traditional Arabic coffee shop in Old Dubai and want to attract more tourists while preserving our authentic atmosphere. What digital marketing strategies would you recommend?",
                "user_id": "dubai_business_owner"
            }
            
            async with self.session.post(
                f"{API_BASE}/chat/message",
                json=message_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("success") and "response" in data.get("data", {}):
                        ai_response = data["data"]["response"]
                        if ai_response and len(ai_response) > 20:  # Should be substantial response
                            self.log_test("Dubai Chat Scenario", True, "AI chat responded to Dubai coffee shop scenario")
                            return True
                        else:
                            self.log_test("Dubai Chat Scenario", False, "AI response too short or empty", data)
                            return False
                    else:
                        self.log_test("Dubai Chat Scenario", False, "Invalid response structure", data)
                        return False
                else:
                    self.log_test("Dubai Chat Scenario", False, f"HTTP {response.status}", await response.text())
                    return False
        except Exception as e:
            self.log_test("Dubai Chat Scenario", False, f"Exception: {str(e)}")
            return False
    
    async def run_dubai_tests(self):
        """Run all Dubai-specific backend tests"""
        print(f"🇦🇪 Starting Dubai/UAE Business Scenario Tests")
        print(f"📍 Backend URL: {BACKEND_URL}")
        print(f"📍 API Base: {API_BASE}")
        print("=" * 60)
        
        print("\n🏢 Testing Dubai Business Scenarios:")
        print("-" * 40)
        await self.test_dubai_restaurant_problem()
        await self.test_uae_ecommerce_problem()
        await self.test_dubai_contact_form_submission()
        await self.test_uae_business_recommendations()
        await self.test_dubai_chat_scenario()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 DUBAI BUSINESS TEST SUMMARY")
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
            print(f"\n🎉 All Dubai business tests passed!")
        
        return failed_tests == 0

async def main():
    """Main test runner"""
    async with DubaiBusinessTester() as tester:
        success = await tester.run_dubai_tests()
        return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)