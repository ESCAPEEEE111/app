from config import settings
import logging
from typing import Dict, Any, Optional
import asyncio

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.api_key = settings.openai_api_key
        self.model = settings.default_ai_model
        self.provider = settings.ai_provider
        
    async def create_chat_session(self, session_id: str, system_message: str = None) -> dict:
        """Create a new chat session (mocked for now)"""
        if not system_message:
            system_message = """You are a helpful AI assistant for NOWHERE Digital, a leading digital marketing agency in Dubai, UAE. 
            
            You help with:
            - Digital marketing strategy
            - Social media marketing
            - Web development
            - AI solutions
            - SEO and content marketing
            - WhatsApp business solutions
            - E-commerce development
            - Lead generation
            
            Always be professional, helpful, and provide actionable insights specific to the UAE market. 
            Use a friendly but professional tone and include relevant examples when possible.
            
            If users ask about services, pricing, or want to book a consultation, guide them to use the booking system or contact form."""
        
        try:
            # Mock chat session for now
            chat = {
                "session_id": session_id,
                "system_message": system_message,
                "api_key": self.api_key,
                "model": self.model,
                "provider": self.provider
            }
            
            return chat
            
        except Exception as e:
            logger.error(f"Error creating chat session: {e}")
            raise

    async def send_chat_message(self, session_id: str, message: str) -> str:
        """Send a message to the AI chat and get response (mocked for now)"""
        try:
            chat = await self.create_chat_session(session_id)
            # Mock AI response for now
            response = f"Thank you for your message: '{message}'. I'm currently being set up and will provide full AI responses soon. In the meantime, please feel free to use our contact form or booking system to get in touch with our team at NOWHERE Digital."
            return response
            
        except Exception as e:
            logger.error(f"Error sending chat message: {e}")
            return "I'm sorry, I'm having trouble processing your request right now. Please try again later or contact our support team."

    async def generate_content(self, content_type: str, prompt: str, additional_context: Dict[str, Any] = None) -> str:
        """Generate content using AI"""
        try:
            # Create content-specific system messages
            system_messages = {
                "blog_post": """You are a content writer for NOWHERE Digital. Create engaging blog posts about digital marketing, 
                web development, and business growth in the UAE market. Include actionable tips and local insights.""",
                
                "social_media": """You are a social media expert for NOWHERE Digital. Create engaging social media content 
                that resonates with UAE audiences. Include relevant hashtags and call-to-actions.""",
                
                "ad_copy": """You are an advertising copywriter for NOWHERE Digital. Create compelling ad copy that converts 
                for the UAE market. Focus on benefits, urgency, and clear call-to-actions.""",
                
                "email_campaign": """You are an email marketing specialist for NOWHERE Digital. Create email campaigns that 
                engage UAE customers and drive conversions. Include personalization and clear CTAs.""",
                
                "web_copy": """You are a web copywriter for NOWHERE Digital. Create website copy that converts visitors 
                into customers. Focus on benefits, credibility, and clear value propositions.""",
                
                "seo_content": """You are an SEO content specialist for NOWHERE Digital. Create SEO-optimized content 
                that ranks well in UAE search results and provides value to readers."""
            }
            
            system_message = system_messages.get(content_type, 
                "You are a content creator for NOWHERE Digital. Create high-quality content based on the given prompt.")
            
            # Add additional context if provided
            if additional_context:
                system_message += f"\n\nAdditional context: {additional_context}"
            
            session_id = f"content_generation_{content_type}"
            chat = await self.create_chat_session(session_id, system_message)
            
            # Mock content generation for now
            response = f"Generated {content_type} content for: '{prompt}'. Full AI content generation will be available once OpenAI integration is configured."
            
            return response
            
        except Exception as e:
            logger.error(f"Error generating content: {e}")
            return "I'm sorry, I couldn't generate the content right now. Please try again later."

    async def generate_service_recommendations(self, user_input: str) -> str:
        """Generate service recommendations based on user input"""
        try:
            system_message = """You are a digital marketing consultant for NOWHERE Digital. Based on the user's business 
            needs, recommend the most suitable services from our portfolio:
            
            Services available:
            - Social Media Marketing (Instagram, TikTok, LinkedIn, YouTube)
            - WhatsApp Business Solutions
            - Web & App Development
            - AI Solutions & Chatbots
            - SEO & Search Marketing
            - Content Marketing
            - E-commerce Solutions
            - Lead Generation
            - Marketing Automation
            - AR/VR Marketing
            - Voice & Audio Marketing
            - Event Marketing
            
            Provide specific recommendations with explanations and suggest next steps."""
            
            session_id = "service_recommendations"
            chat = await self.create_chat_session(session_id, system_message)
            
            # Mock service recommendations for now
            response = f"Based on your input: '{user_input}', we recommend our comprehensive digital marketing services including Social Media Marketing, Web Development, and SEO. Please contact us for a detailed consultation."
            
            return response
            
        except Exception as e:
            logger.error(f"Error generating service recommendations: {e}")
            return "I'm sorry, I couldn't generate recommendations right now. Please contact our team directly for personalized service recommendations."

    async def analyze_market_trends(self, industry: str, location: str = "UAE") -> str:
        """Analyze market trends for a specific industry"""
        try:
            system_message = f"""You are a market research analyst for NOWHERE Digital. Analyze current digital marketing 
            trends for the {industry} industry in {location}. Provide insights on:
            
            - Current market trends
            - Digital marketing opportunities
            - Competitive landscape
            - Consumer behavior patterns
            - Recommended strategies
            - ROI potential
            
            Focus on actionable insights that can help businesses grow."""
            
            session_id = f"market_analysis_{industry}"
            chat = await self.create_chat_session(session_id, system_message)
            
            # Mock market analysis for now
            response = f"Market analysis for {industry} in {location}: Growing digital transformation opportunities with strong mobile and social media adoption. Contact us for detailed market insights."
            
            return response
            
        except Exception as e:
            logger.error(f"Error analyzing market trends: {e}")
            return "I'm sorry, I couldn't analyze the market trends right now. Please try again later."

    async def generate_strategy_proposal(self, business_info: Dict[str, Any]) -> str:
        """Generate a digital marketing strategy proposal"""
        try:
            system_message = """You are a digital marketing strategist for NOWHERE Digital. Create comprehensive 
            digital marketing strategy proposals tailored to the UAE market. Include:
            
            - Situation analysis
            - Target audience identification
            - Recommended channels and tactics
            - Timeline and milestones
            - Budget considerations
            - Expected outcomes
            - Next steps
            
            Make the proposal professional and actionable."""
            
            session_id = "strategy_proposal"
            chat = await self.create_chat_session(session_id, system_message)
            
            # Mock strategy proposal for now
            business_name = business_info.get('business_name', 'Your Business')
            industry = business_info.get('industry', 'Not specified')
            response = f"Digital Marketing Strategy Proposal for {business_name} ({industry}): We recommend a comprehensive approach including social media marketing, SEO optimization, and lead generation tailored for the UAE market. Contact us for a detailed proposal."
            
            return response
            
        except Exception as e:
            logger.error(f"Error generating strategy proposal: {e}")
            return "I'm sorry, I couldn't generate the strategy proposal right now. Please contact our team for a personalized proposal."

# Create global AI service instance
ai_service = AIService()