import React from 'react';
import { Link } from 'react-router-dom';
import { 
  ArrowRight, CheckCircle, Megaphone, MessageCircle, Globe, 
  Search, Camera, ShoppingBag, Brain, BarChart3, Eye, Shield, 
  Volume2, Calendar, Plane, Building, Heart, Home, Rocket, 
  Smartphone, Zap 
} from 'lucide-react';

const ServicesPage = () => {
  // Simple test data to isolate the issue
  const testServices = [
    {
      id: 1,
      title: "Web Development",
      description: "Custom web solutions",
      features: ["Responsive Design", "Fast Loading", "SEO Optimized"],
      pricing: "AED 5,000",
      icon: "Globe",
      category: "development"
    },
    {
      id: 2,
      title: "Digital Marketing",
      description: "Comprehensive marketing solutions",
      features: ["Social Media", "Content Marketing", "Analytics"],
      pricing: "AED 3,000",
      icon: "Megaphone",
      category: "marketing"
    }
  ];

  const iconMap = {
    Megaphone, MessageCircle, Globe, Search, Camera, ShoppingBag, 
    Brain, BarChart3, Eye, Shield, Volume2, Calendar, Plane, 
    Building, Heart, Home, Rocket, Smartphone, Zap
  };

  return (
    <div className="min-h-screen bg-black text-green-400 p-8">
      {/* Navigation Spacer */}
      <div className="pt-20"></div>
      
      {/* Page Header */}
      <div className="text-center mb-16">
        <h1 className="text-4xl lg:text-6xl font-bold mb-6 font-mono text-cyan-400">
          COMPREHENSIVE SERVICES
        </h1>
        <p className="text-xl text-green-300 max-w-4xl mx-auto font-mono leading-relaxed mb-8">
          Full-spectrum digital solutions designed for the modern business landscape.
        </p>
      </div>

      {/* Services Grid */}
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {testServices.map((service) => {
            const IconComponent = iconMap[service.icon];
            return (
              <div
                key={service.id}
                className="bg-gray-900 border border-green-500/30 rounded-lg p-6 hover:border-green-500 transition-all duration-300"
              >
                <div className="flex items-center space-x-3 mb-4">
                  {IconComponent && <IconComponent className="w-8 h-8 text-cyan-400" />}
                  <h3 className="text-xl font-bold text-green-400 font-mono">
                    {service.title}
                  </h3>
                </div>
                
                <p className="text-green-300/70 font-mono text-sm mb-4">
                  {service.description}
                </p>
                
                <ul className="space-y-2 mb-6">
                  {service.features.map((feature, idx) => (
                    <li key={idx} className="flex items-center space-x-2 text-sm">
                      <CheckCircle className="w-4 h-4 text-cyan-400 flex-shrink-0" />
                      <span className="text-green-300/80 font-mono">{feature}</span>
                    </li>
                  ))}
                </ul>
                
                <div className="flex items-center justify-between">
                  <span className="text-cyan-400 font-mono font-bold">
                    {service.pricing}
                  </span>
                  <button className="bg-green-600/20 border border-green-500/40 text-green-400 hover:bg-green-600/30 font-mono text-sm px-4 py-2 rounded">
                    LEARN_MORE
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* CTA Section */}
      <div className="max-w-4xl mx-auto text-center mt-16">
        <div className="bg-green-500/10 border border-green-500/30 rounded-lg p-12">
          <h2 className="text-3xl font-bold mb-6 font-mono text-green-400">
            NEED CUSTOM SOLUTION?
          </h2>
          <p className="text-xl text-green-300/80 mb-8 font-mono">
            Let our AI analyze your business needs and recommend the perfect service combination
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/ai-solver">
              <button className="bg-cyan-500 text-black hover:bg-cyan-400 font-mono font-bold px-8 py-4 text-lg rounded">
                GET_CUSTOM_RECOMMENDATIONS
                <ArrowRight className="inline w-5 h-5 ml-2" />
              </button>
            </Link>
            <Link to="/contact">
              <button className="border border-green-500 text-green-400 hover:bg-green-500/10 font-mono font-bold px-8 py-4 text-lg rounded">
                SPEAK_WITH_EXPERT
              </button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ServicesPage;

const ServicesPage = () => {
  return (
    <MobileMatrixOptimizer className="min-h-screen bg-black text-matrix-green relative overflow-hidden">
      {/* Clean background */}
      <div className="fixed inset-0 z-0 bg-black" />
      
      {/* Page Header */}
      <section className="pt-32 pb-12 relative z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <Badge className="bg-gradient-to-r from-matrix-green/20 to-matrix-cyan/20 text-matrix-green border-matrix-green/40 font-mono mb-6 px-6 py-3">
            💼 COMPREHENSIVE SERVICE PORTFOLIO
          </Badge>
          
          <h1 className="text-4xl lg:text-6xl font-bold mb-6 font-mono">
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
              COMPREHENSIVE
            </span>
            <br />
            <span className="text-white">ARSENAL</span>
          </h1>
          
          <p className="text-xl text-matrix-green/80 max-w-4xl mx-auto font-mono leading-relaxed mb-8">
            WEB_DEVELOPMENT | LEAD_GENERATION | AI_AGENTS | UAE_MARKET_DOMINANCE
            <br />
            Full-spectrum digital solutions designed for the modern business landscape.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/ai-solver">
              <Button className="bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan text-black hover:from-matrix-bright-cyan hover:to-matrix-cyan font-mono font-bold px-8 py-4 text-lg">
                🧠 GET_SERVICE_RECOMMENDATIONS
                <ArrowRight className="ml-2 w-5 h-5" />
              </Button>
            </Link>
            
            <Link to="/contact">
              <Button variant="outline" className="border-matrix-green text-matrix-green hover:bg-matrix-green/10 font-mono font-bold px-8 py-4 text-lg">
                📞 DISCUSS_PROJECT
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Core Services Section */}
      <section className="py-20 relative z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl lg:text-4xl font-bold mb-6 font-mono">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
                CORE_SERVICES
              </span>
            </h2>
            <p className="text-lg text-matrix-green/80 font-mono">
              Comprehensive digital solutions tailored for your success
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, index) => {
              const IconComponent = iconMap[service.icon];
              return (
                <Card
                  key={service.id}
                  className="bg-black/50 border-matrix-green/30 hover:border-matrix-green transition-all duration-300 transform hover:scale-105 hover:-translate-y-2 group backdrop-blur-sm"
                >
                  <CardHeader>
                    <div className="flex items-center space-x-3 mb-3">
                      {IconComponent && <IconComponent className="w-8 h-8 text-matrix-cyan group-hover:text-white transition-colors" />}
                      <Badge className="bg-matrix-green/20 text-matrix-green border-matrix-green/40 font-mono text-xs">
                        {service.category.toUpperCase()}
                      </Badge>
                    </div>
                    <CardTitle className="text-matrix-green group-hover:text-white font-mono text-lg transition-colors">
                      {service.title}
                    </CardTitle>
                    <CardDescription className="text-matrix-green/70 font-mono text-sm">
                      {service.description}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="space-y-2 mb-6">
                      {service.features.map((feature, idx) => (
                        <li key={idx} className="flex items-center space-x-2 text-sm">
                          <CheckCircle className="w-4 h-4 text-matrix-cyan flex-shrink-0" />
                          <span className="text-matrix-green/80 font-mono">{feature}</span>
                        </li>
                      ))}
                    </ul>
                    <div className="flex items-center justify-between">
                      <span className="text-matrix-bright-cyan font-mono font-bold">
                        {service.pricing}
                      </span>
                      <Button 
                        size="sm"
                        className="bg-matrix-dark-cyan/20 border border-matrix-cyan/40 text-matrix-cyan hover:bg-matrix-cyan/10 font-mono text-xs"
                      >
                        LEARN_MORE
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* Specialized Services Section */}
      <section className="py-20 relative z-10 bg-gradient-to-r from-matrix-green/5 to-matrix-cyan/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl lg:text-4xl font-bold mb-6 font-mono">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
                SPECIALIZED_SOLUTIONS
              </span>
            </h2>
            <p className="text-lg text-matrix-green/80 font-mono">
              Advanced services for specific industry needs
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {specializedServices.map((service, index) => {
              const IconComponent = iconMap[service.icon];
              return (
                <Card
                  key={service.id}
                  className="bg-black/30 border-matrix-green/20 hover:border-matrix-green/40 transition-all duration-300 text-center group backdrop-blur-sm"
                >
                  <CardHeader>
                    <div className="mx-auto mb-4">
                      {IconComponent && <IconComponent className="w-10 h-10 text-matrix-cyan group-hover:text-white transition-colors mx-auto" />}
                    </div>
                    <CardTitle className="text-matrix-green group-hover:text-white font-mono text-base transition-colors">
                      {service.title}
                    </CardTitle>
                    <CardDescription className="text-matrix-green/70 font-mono text-xs">
                      {service.description}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="space-y-1 mb-4">
                      {service.features.slice(0, 3).map((feature, idx) => (
                        <li key={idx} className="text-xs text-matrix-green/80 font-mono">
                          • {feature}
                        </li>
                      ))}
                    </ul>
                    <Button 
                      size="sm"
                      className="w-full bg-matrix-dark-cyan/20 border border-matrix-cyan/40 text-matrix-cyan hover:bg-matrix-cyan/10 font-mono text-xs"
                    >
                      EXPLORE
                    </Button>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* Service Packages */}
      <section className="py-20 relative z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl lg:text-4xl font-bold mb-6 font-mono">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
                SERVICE_PACKAGES
              </span>
            </h2>
            <p className="text-lg text-matrix-green/80 font-mono">
              Bundled solutions for maximum efficiency and value
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Startup Package */}
            <Card className="bg-black/60 border-matrix-green/30 hover:border-matrix-cyan/60 transition-all duration-300 group">
              <CardHeader className="text-center">
                <Badge className="bg-gradient-to-r from-matrix-green to-matrix-cyan text-black font-mono mb-4 px-4 py-2 mx-auto">
                  STARTUP_PACKAGE
                </Badge>
                <CardTitle className="text-2xl font-bold text-matrix-green font-mono group-hover:text-white transition-colors">
                  DIGITAL_LAUNCH
                </CardTitle>
                <div className="text-3xl font-bold text-matrix-bright-cyan font-mono">
                  AED 15,000
                  <span className="text-sm text-matrix-green/70">/month</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3 mb-8">
                  {[
                    "Professional Website",
                    "Social Media Setup",
                    "Basic SEO Optimization",
                    "Lead Generation System",
                    "Monthly Analytics Report"
                  ].map((feature, idx) => (
                    <li key={idx} className="flex items-center space-x-2">
                      <CheckCircle className="w-4 h-4 text-matrix-cyan flex-shrink-0" />
                      <span className="text-matrix-green/80 font-mono text-sm">{feature}</span>
                    </li>
                  ))}
                </ul>
                <Button className="w-full bg-matrix-green/20 border border-matrix-green text-matrix-green hover:bg-matrix-green/10 font-mono">
                  GET_STARTED
                </Button>
              </CardContent>
            </Card>

            {/* Growth Package */}
            <Card className="bg-black/60 border-matrix-cyan/50 hover:border-matrix-bright-cyan/60 transition-all duration-300 group transform scale-105">
              <CardHeader className="text-center">
                <Badge className="bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan text-black font-mono mb-4 px-4 py-2 mx-auto">
                  GROWTH_PACKAGE
                </Badge>
                <CardTitle className="text-2xl font-bold text-matrix-cyan font-mono group-hover:text-white transition-colors">
                  MARKET_DOMINATION
                </CardTitle>
                <div className="text-3xl font-bold text-matrix-bright-cyan font-mono">
                  AED 35,000
                  <span className="text-sm text-matrix-green/70">/month</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3 mb-8">
                  {[
                    "Everything in Startup",
                    "AI Chatbot Integration",
                    "Advanced Marketing Automation",
                    "Mobile App Development",
                    "24/7 Support & Monitoring"
                  ].map((feature, idx) => (
                    <li key={idx} className="flex items-center space-x-2">
                      <CheckCircle className="w-4 h-4 text-matrix-cyan flex-shrink-0" />
                      <span className="text-matrix-green/80 font-mono text-sm">{feature}</span>
                    </li>
                  ))}
                </ul>
                <Button className="w-full bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan text-black hover:from-matrix-bright-cyan hover:to-matrix-cyan font-mono font-bold">
                  MOST_POPULAR
                </Button>
              </CardContent>
            </Card>

            {/* Enterprise Package */}
            <Card className="bg-black/60 border-matrix-green/30 hover:border-matrix-cyan/60 transition-all duration-300 group">
              <CardHeader className="text-center">
                <Badge className="bg-gradient-to-r from-purple-500 to-pink-500 text-white font-mono mb-4 px-4 py-2 mx-auto">
                  ENTERPRISE_PACKAGE
                </Badge>
                <CardTitle className="text-2xl font-bold text-matrix-green font-mono group-hover:text-white transition-colors">
                  COMPLETE_ECOSYSTEM
                </CardTitle>
                <div className="text-3xl font-bold text-matrix-bright-cyan font-mono">
                  AED 75,000+
                  <span className="text-sm text-matrix-green/70">/month</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3 mb-8">
                  {[
                    "Everything in Growth",
                    "Custom AI Solutions",
                    "AR/VR Integration",
                    "Dedicated Account Manager",
                    "White-label Solutions"
                  ].map((feature, idx) => (
                    <li key={idx} className="flex items-center space-x-2">
                      <CheckCircle className="w-4 h-4 text-matrix-cyan flex-shrink-0" />
                      <span className="text-matrix-green/80 font-mono text-sm">{feature}</span>
                    </li>
                  ))}
                </ul>
                <Button className="w-full bg-matrix-green/20 border border-matrix-green text-matrix-green hover:bg-matrix-green/10 font-mono">
                  CONTACT_SALES
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 relative z-10">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-gradient-to-r from-matrix-green/10 to-matrix-cyan/10 border border-matrix-green/30 rounded-lg p-12 backdrop-blur-sm">
            <h2 className="text-3xl lg:text-4xl font-bold mb-6 font-mono">
              <span className="text-matrix-green">NEED_CUSTOM</span>
              <br />
              <span className="text-white">SOLUTION?</span>
            </h2>
            
            <p className="text-xl text-matrix-green/80 mb-8 font-mono">
              Let our AI analyze your business needs and recommend the perfect service combination
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/ai-solver">
                <Button className="bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan text-black hover:from-matrix-bright-cyan hover:to-matrix-cyan font-mono font-bold px-8 py-4 text-lg">
                  🧠 GET_CUSTOM_RECOMMENDATIONS
                  <ArrowRight className="ml-2 w-5 h-5" />
                </Button>
              </Link>
              
              <Link to="/contact">
                <Button variant="outline" className="border-matrix-green text-matrix-green hover:bg-matrix-green/10 font-mono font-bold px-8 py-4 text-lg">
                  📞 SPEAK_WITH_EXPERT
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>
    </MobileMatrixOptimizer>
  );
};

export default ServicesPage;