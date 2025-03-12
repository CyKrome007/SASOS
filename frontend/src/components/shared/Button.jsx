import React from 'react';
import {useNavigate} from "react-router-dom";

export const Button = ({content = 'FIND OUT MORE'}, to='/predict') => {
    const navigate = useNavigate();
    const onClick = (e) => {
        console.log('clicked');
        navigate('/predict');
    }
  return (
    <button
        onClick={onClick}
        style={{
          backgroundColor: '#FFA500', // Orange color
          color: 'white',
          padding: '12px 24px',
          border: 'none',
          cursor: 'pointer',
          fontSize: '16px',
          fontWeight: 'bold',
          display: 'inline-flex',
          alignItems: 'center',
          justifyContent: 'center',
            borderTopLeftRadius: '2rem',
            borderBottomRightRadius: '2rem',
          // Add any additional styling you want here, like margin, etc.
        }}
    >
        {content}
    </button>
  );
};

// export default Button;