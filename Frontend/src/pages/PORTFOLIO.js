import { Link } from "react-router-dom";
import styles from "./PORTFOLIO.module.css";

const PORTFOLIO = () => {
  return (
    <div className={styles.portfolio}>
      <div className={styles.frame}>
        <div className={styles.frameChild} />
      </div>
      <img
        className={styles.microsoftteamsImage2Icon}
        alt=""
        src="/microsoftteamsimage-2@2x.png"
      />
      <div className={styles.portfolioChild} />
      <Link className={styles.appLogoInspiraton9} to="/1home">
        <img className={styles.vectorIcon} alt="" src="/vector181@2x.png" />
        <img className={styles.vectorIcon1} alt="" src="/vector182@2x.png" />
      </Link>
      <Link className={styles.loginSignUpWrapper} to="/4login">
        <div className={styles.loginSign}>lOGIN | SIGN UP</div>
      </Link>
      <Link className={styles.cryptoWrapper} to="/2crypto">
        <div className={styles.loginSign}>Crypto</div>
      </Link>
      <Link className={styles.stocksWrapper} to="/5stocks">
        <div className={styles.loginSign}>stocks</div>
      </Link>
      <div className={styles.portfolioItem} />
    </div>
  );
};

export default PORTFOLIO;
