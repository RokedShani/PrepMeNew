import "../styles/globals.css";
import type { AppProps } from "next/app";
import { createTheme } from "@nextui-org/react";
// import Script from 'next/script';
import { ThemeProvider as NextThemesProvider } from 'next-themes';
// import Particles, { ISourceOptions } from "react-tsparticles";


const darkTheme = createTheme({
  type: "dark",
  theme: {
    colors: {
    }, 
  },
});

function MyApp({ Component, pageProps }: AppProps) {
  // return <Component {...pageProps} />
  return (
    <NextThemesProvider
    defaultTheme="system"
    attribute="class"
    value={{
      dark: darkTheme.className
    }}
  >
    <Component {...pageProps}>
    <div className="d-flex flex-column justify-content-center w-100 h-100">

	<div className="d-flex flex-column justify-content-center align-items-center">
		<h1 className="fw-light text-white m-0">Pure CSS Gradient Background Animation</h1>
		<div className="btn-group my-5">
			<a href="https://codepen-api-export-production.s3.us-west-2.amazonaws.com/zip/PEN/pyBNzX/1578778289271/pure-css-gradient-background-animation.zip" class="btn btn-outline-light" aria-current="page"><i class="fas fa-file-download me-2"></i> SOURCE CODE</a>
			<a href="https://codepen.io/P1N2O/full/pyBNzX" className="btn btn-outline-light">FULL SCREEN <i className="fas fa-expand ms-2"></i></a>
		</div>
		<a href="https://manuel.pinto.dev" className="text-decoration-none">
			<h5 className="fw-light text-white m-0">— Pen by Manuel Pinto —</h5>
		</a>
	</div>
</div>


      </Component>
</NextThemesProvider>

  );
} 
  

export default MyApp;
