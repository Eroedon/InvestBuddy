import { useCallback } from "react";
import { Link } from "react-router-dom";
import styles from "./CRYPTO1.module.css";

const CRYPTO1 = () => {
  const onFrameContainer1Click = useCallback(() => {
    const anchor = document.querySelector("[data-scroll-to='watchlistText']");
    if (anchor) {
      anchor.scrollIntoView({ block: "start", behavior: "smooth" });
    }
  }, []);

  return (
    <div className={styles.crypto}>
      <img
        className={styles.microsoftteamsImage2Icon}
        alt=""
        src="/microsoftteamsimage-2@2x.png"
      />
      <div className={styles.cryptoChild} />
      <Link className={styles.frame} to="/3portfolio">
        <Link className={styles.portfolioWrapper} to="/3portfolio">
          <div className={styles.portfolio}>Portfolio</div>
        </Link>
      </Link>
      <Link className={styles.loginSignUpWrapper} to="/4login">
        <div className={styles.loginSign}>lOGIN | SIGN UP</div>
      </Link>
      <Link className={styles.appLogoInspiraton9} to="/1home">
        <img className={styles.vectorIcon} alt="" src="/vector181@2x.png" />
        <img className={styles.vectorIcon1} alt="" src="/vector183@2x.png" />
      </Link>
      <div className={styles.cryptoItem} />
      <a
        className={styles.allCryptocurrencies}
        href="https://coinmarketcap.com/currencies/"
      >
        All Cryptocurrencies
      </a>
      <div className={styles.cryptoInner} />
      <div className={styles.lineDiv} />
      <div className={styles.name}>Name</div>
      <div className={styles.symbol}>Symbol</div>
      <div className={styles.marketCap}>Market Cap</div>
      <div className={styles.price}>Price</div>
      <div className={styles.h}>%1h</div>
      <div className={styles.h1}>%24h</div>
      <div className={styles.d}>%7d</div>
      <div className={styles.curcilatingSupply}>Curcilating Supply</div>
      <div className={styles.bitcoin}>Bitcoin</div>
      <div className={styles.btc}>BTC</div>
      <div className={styles.div}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div1}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc1}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div2}>-0,59%</div>
      <div className={styles.div3}>0,42%</div>
      <div className={styles.div4}>11,62%</div>
      <div className={styles.cryptoChild1} />
      <div className={styles.bitcoin1}>Bitcoin</div>
      <div className={styles.btc3}>BTC</div>
      <div className={styles.div5}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div6}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc4}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div7}>-0,59%</div>
      <div className={styles.div8}>0,42%</div>
      <div className={styles.div9}>11,62%</div>
      <div className={styles.cryptoChild2} />
      <div className={styles.bitcoin2}>Bitcoin</div>
      <div className={styles.btc6}>BTC</div>
      <div className={styles.div10}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div11}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc7}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div12}>-0,59%</div>
      <div className={styles.div13}>0,42%</div>
      <div className={styles.div14}>11,62%</div>
      <div className={styles.cryptoChild3} />
      <div className={styles.bitcoin3}>Bitcoin</div>
      <div className={styles.btc9}>BTC</div>
      <div className={styles.div15}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div16}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc10}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div17}>-0,59%</div>
      <div className={styles.div18}>0,42%</div>
      <div className={styles.div19}>11,62%</div>
      <div className={styles.cryptoChild4} />
      <div className={styles.bitcoin4}>Bitcoin</div>
      <div className={styles.btc12}>BTC</div>
      <div className={styles.div20}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div21}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc13}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div22}>-0,59%</div>
      <div className={styles.div23}>0,42%</div>
      <div className={styles.div24}>11,62%</div>
      <div className={styles.bitcoin}>Bitcoin</div>
      <div className={styles.btc}>BTC</div>
      <div className={styles.div}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div1}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc1}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div2}>-0,59%</div>
      <div className={styles.div3}>0,42%</div>
      <div className={styles.div4}>11,62%</div>
      <div className={styles.bitcoin1}>Bitcoin</div>
      <div className={styles.btc3}>BTC</div>
      <div className={styles.div5}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div6}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc4}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div7}>-0,59%</div>
      <div className={styles.div8}>0,42%</div>
      <div className={styles.div9}>11,62%</div>
      <div className={styles.bitcoin2}>Bitcoin</div>
      <div className={styles.btc6}>BTC</div>
      <div className={styles.div10}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div11}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc7}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div12}>-0,59%</div>
      <div className={styles.div13}>0,42%</div>
      <div className={styles.div14}>11,62%</div>
      <div className={styles.bitcoin3}>Bitcoin</div>
      <div className={styles.btc9}>BTC</div>
      <div className={styles.div15}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div16}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc10}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div17}>-0,59%</div>
      <div className={styles.div18}>0,42%</div>
      <div className={styles.div19}>11,62%</div>
      <div className={styles.div21}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.cryptoChild5} />
      <div className={styles.cryptoChild6} />
      <div className={styles.cryptoChild7} />
      <div className={styles.cryptoChild8} />
      <div className={styles.cryptoChild9} />
      <div className={styles.bitcoin9}>Bitcoin</div>
      <div className={styles.btc27}>BTC</div>
      <div className={styles.div46}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div47}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc28}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div48}>-0,59%</div>
      <div className={styles.div49}>0,42%</div>
      <div className={styles.div50}>11,62%</div>
      <div className={styles.bitcoin10}>Bitcoin</div>
      <div className={styles.btc30}>BTC</div>
      <div className={styles.div51}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div52}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc31}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div53}>-0,59%</div>
      <div className={styles.div54}>0,42%</div>
      <div className={styles.div55}>11,62%</div>
      <div className={styles.bitcoin11}>Bitcoin</div>
      <div className={styles.btc33}>BTC</div>
      <div className={styles.div56}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div57}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc34}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div58}>-0,59%</div>
      <div className={styles.div59}>0,42%</div>
      <div className={styles.div60}>11,62%</div>
      <div className={styles.bitcoin12}>Bitcoin</div>
      <div className={styles.btc36}>BTC</div>
      <div className={styles.div61}>
        <span className={styles.txt}>
          <p className={styles.p}>$674,207,761,539</p>
        </span>
      </div>
      <div className={styles.div62}>
        <span className={styles.txt}>
          <p className={styles.p}>$34,524.46</p>
        </span>
      </div>
      <div className={styles.btc37}>
        <span className={styles.btcTxt}>
          <p className={styles.p}>19.528.406 BTC</p>
        </span>
      </div>
      <div className={styles.div63}>-0,59%</div>
      <div className={styles.div64}>0,42%</div>
      <div className={styles.div65}>11,62%</div>
      <div className={styles.watchlistParent} onClick={onFrameContainer1Click}>
        <div className={styles.watchlist} data-scroll-to="watchlistText">
          {" "}
          Watchlist
        </div>
        <div className={styles.vectorWrapper}>
          <img className={styles.vectorIcon2} alt="" src="/vector6@2x.png" />
        </div>
      </div>
      <div className={styles.filters}>Filters</div>
    </div>
  );
};

export default CRYPTO1;
