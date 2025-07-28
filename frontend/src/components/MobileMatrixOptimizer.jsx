import React, { useState, useEffect } from 'react';

const MobileMatrixOptimizer = ({ children, className = "" }) => {
  const [isMobile, setIsMobile] = useState(false);
  const [orientation, setOrientation] = useState('portrait');
  const [touchSupported, setTouchSupported] = useState(false);

  useEffect(() => {
    // Detect mobile and touch devices
    const checkDevice = () => {
      const mobile = window.innerWidth <= 768 || /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
      const touch = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
      const orient = window.innerHeight > window.innerWidth ? 'portrait' : 'landscape';
      
      setIsMobile(mobile);
      setTouchSupported(touch);
      setOrientation(orient);
    };

    checkDevice();
    window.addEventListener('resize', checkDevice);
    window.addEventListener('orientationchange', checkDevice);

    return () => {
      window.removeEventListener('resize', checkDevice);
      window.removeEventListener('orientationchange', checkDevice);
    };
  }, []);

  // Mobile-specific Matrix effects optimization
  useEffect(() => {
    if (isMobile) {
      // Reduce animation intensity on mobile for performance
      document.documentElement.style.setProperty('--matrix-animation-speed', '0.5s');
      document.documentElement.style.setProperty('--matrix-particle-count', '30');
      document.documentElement.style.setProperty('--matrix-effects-opacity', '0.6');
    } else {
      // Full effects on desktop
      document.documentElement.style.setProperty('--matrix-animation-speed', '1s');
      document.documentElement.style.setProperty('--matrix-particle-count', '100');
      document.documentElement.style.setProperty('--matrix-effects-opacity', '0.8');
    }
  }, [isMobile]);

  const mobileClasses = isMobile ? 'mobile-optimized' : 'desktop-full';
  const orientationClasses = `orientation-${orientation}`;
  const touchClasses = touchSupported ? 'touch-enabled' : 'touch-disabled';

  return (
    <div className={`${className} ${mobileClasses} ${orientationClasses} ${touchClasses}`}>
      {/* Mobile Navigation Optimization */}
      {isMobile && (
        <style jsx>{`
          .mobile-optimized {
            /* Optimize scrolling on mobile */
            -webkit-overflow-scrolling: touch;
            scroll-behavior: smooth;
          }
          
          .mobile-optimized .matrix-rain {
            /* Reduce matrix rain intensity on mobile */
            opacity: 0.4;
            animation-duration: 2s;
          }
          
          .mobile-optimized .matrix-particles {
            /* Fewer particles on mobile */
            display: none;
          }
          
          .mobile-optimized .matrix-waves {
            /* Simpler waves on mobile */
            opacity: 0.3;
          }
          
          .mobile-optimized .text-5xl,
          .mobile-optimized .text-6xl,
          .mobile-optimized .text-7xl {
            /* Responsive text scaling */
            font-size: clamp(2rem, 8vw, 4rem) !important;
          }
          
          .mobile-optimized .grid {
            /* Better grid layouts on mobile */
            grid-template-columns: 1fr !important;
            gap: 1rem !important;
          }
          
          .mobile-optimized .p-8,
          .mobile-optimized .px-8,
          .mobile-optimized .py-8 {
            /* Reduced padding on mobile */
            padding: 1rem !important;
          }
          
          .mobile-optimized .space-x-8 > :not([hidden]) ~ :not([hidden]) {
            /* Reduced spacing on mobile */
            margin-left: 1rem !important;
          }
          
          .touch-enabled button,
          .touch-enabled .cursor-pointer {
            /* Larger touch targets */
            min-height: 44px;
            min-width: 44px;
          }
          
          .orientation-landscape .min-h-screen {
            /* Adjust for landscape orientation */
            min-height: 100vh;
          }
          
          .orientation-portrait .grid-cols-2 {
            /* Single column in portrait */
            grid-template-columns: 1fr !important;
          }
          
          /* Mobile-specific animations */
          @media (max-width: 768px) {
            .matrix-text-glow {
              animation-duration: 3s;
            }
            
            .animate-pulse {
              animation-duration: 3s;
            }
            
            .transform {
              transform: none !important;
            }
            
            .hover\\:scale-105:hover {
              transform: none !important;
            }
          }
          
          /* Reduce motion for users who prefer it */
          @media (prefers-reduced-motion: reduce) {
            .matrix-text-glow,
            .animate-pulse,
            .animate-ping {
              animation: none !important;
            }
          }
        `}</style>
      )}

      {children}

      {/* Mobile Performance Monitor */}
      {isMobile && process.env.NODE_ENV === 'development' && (
        <div className="fixed bottom-2 left-2 bg-black/80 text-matrix-green text-xs p-2 rounded font-mono border border-matrix-green/30 z-50">
          <div>Mobile: {isMobile ? 'YES' : 'NO'}</div>
          <div>Touch: {touchSupported ? 'YES' : 'NO'}</div>
          <div>Orient: {orientation.toUpperCase()}</div>
          <div>Width: {window.innerWidth}px</div>
        </div>
      )}
    </div>
  );
};

// Custom hook for mobile detection
export const useMobile = () => {
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth <= 768);
    };

    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  return isMobile;
};

// Mobile-optimized Matrix components
export const MobileMatrixRain = ({ className = "" }) => {
  const isMobile = useMobile();
  
  if (isMobile) {
    return (
      <div className={`absolute inset-0 pointer-events-none opacity-30 ${className}`}>
        <div className="matrix-mobile-rain" />
        <style jsx>{`
          .matrix-mobile-rain {
            background: linear-gradient(
              180deg,
              transparent 0%,
              rgba(0, 255, 65, 0.1) 50%,
              transparent 100%
            );
            background-size: 100% 200px;
            animation: mobile-rain 4s linear infinite;
            height: 100%;
            width: 100%;
          }
          
          @keyframes mobile-rain {
            0% { background-position: 0 -200px; }
            100% { background-position: 0 calc(100vh + 200px); }
          }
        `}</style>
      </div>
    );
  }
  
  return null;
};

export const MobileMatrixText = ({ children, className = "" }) => {
  const isMobile = useMobile();
  
  return (
    <div className={`${className} ${isMobile ? 'mobile-matrix-text' : ''}`}>
      {children}
      {isMobile && (
        <style jsx>{`
          .mobile-matrix-text {
            font-size: clamp(1.5rem, 6vw, 3rem);
            line-height: 1.2;
            text-align: center;
          }
          
          .mobile-matrix-text .matrix-text-glow {
            text-shadow: 0 0 10px #00FF41;
            animation: mobile-glow 2s ease-in-out infinite alternate;
          }
          
          @keyframes mobile-glow {
            from { text-shadow: 0 0 10px #00FF41; }
            to { text-shadow: 0 0 20px #00FF41, 0 0 30px #00FF41; }
          }
        `}</style>
      )}
    </div>
  );
};

export default MobileMatrixOptimizer;