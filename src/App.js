import { useEffect } from "react";
import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import HOME from "./pages/HOME";
import STOCKS from "./pages/STOCKS";
import LogIn from "./pages/LogIn";
import PORTFOLIO from "./pages/PORTFOLIO";
import CRYPTO1 from "./pages/CRYPTO1";
import IllustrationBloggingBlogCo from "./pages/IllustrationBloggingBlogCo";

function App() {
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/5stocks":
        title = "";
        metaDescription = "";
        break;
      case "/4login":
        title = "";
        metaDescription = "";
        break;
      case "/3portfolio":
        title = "";
        metaDescription = "";
        break;
      case "/2crypto":
        title = "";
        metaDescription = "";
        break;
      case "/-illustration-blogging-blog-computer-desk-laptop-work-office":
        title = "";
        metaDescription = "";
        break;
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <Routes>
      <Route path="/" element={<HOME />} />
      <Route path="/5stocks" element={<STOCKS />} />
      <Route path="/4login" element={<LogIn />} />
      <Route path="/3portfolio" element={<PORTFOLIO />} />
      <Route path="/2crypto" element={<CRYPTO1 />} />
      <Route
        path="/-illustration-blogging-blog-computer-desk-laptop-work-office"
        element={<IllustrationBloggingBlogCo />}
      />
    </Routes>
  );
}
export default App;
