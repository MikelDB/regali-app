import React from 'react';
import { createGlobalStyle } from 'styled-components';
import { Dashboard } from './pages';

const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
`;

function App(): React.ReactElement {
  return (
    <>
      <GlobalStyle />
      <Dashboard />
    </>
  );
}

export default App;
