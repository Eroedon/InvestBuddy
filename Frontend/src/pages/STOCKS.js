import React from 'react';
import { Link } from 'react-router-dom';
import styles from './STOCKS.module.css';

class STOCKS extends React.Component {
    render() {
        return (
            <div className={styles.stocks}>
                <div className={styles.frame}>
                    <div className={styles.frameChild} />
                </div>
                <img
                    className={styles.microsoftteamsImage2Icon}
                    alt=""
                    src="/microsoftteamsimage-2@2x.png"
                />
                <div className={styles.stocksChild} />
                <Link className={styles.appLogoInspiraton9} to="/1home">
                    <img className={styles.vectorIcon} alt="" src="/vector181@2x.png" />
                    <img className={styles.vectorIcon1} alt="" src="/vector182@2x.png" />
                </Link>
                <Link className={styles.loginSignUpWrapper} to="/4login">
                    <div className={styles.loginSign}>LOGIN | SIGN UP</div>
                </Link>
                <Link className={styles.cryptoWrapper} to="/2crypto">
                    <div className={styles.loginSign}>Crypto</div>
                </Link>
                <Link className={styles.portfolioWrapper} to="/3portfolio">
                    <div className={styles.loginSign}>Portfolio</div>
                </Link>
                <div className={styles.thePageIsCurrentlyUnderMaWrapper}>
                    <div className={styles.thePageIs}>
                        The page is currently under maintenance
                    </div>
                </div>
            </div>
        );
    }
}

export default STOCKS;
