import { Link } from "react-router-dom";
import styles from "./HOME.module.css";

const HOME = () => {
  return (
    <div className={styles.home}>
      <img
        className={styles.microsoftteamsImage1Icon}
        alt=""
        src="/microsoftteamsimage-2@2x.png"
      />
      <div className={styles.homeChild} />
      <Link className={styles.frame} to="/3portfolio">
        <Link className={styles.portfolioWrapper} to="/3portfolio">
          <div className={styles.portfolio}>Portfolio</div>
        </Link>
      </Link>
      <Link className={styles.frame1} to="/2crypto">
        <Link className={styles.portfolioWrapper} to="/crypto">
          <div className={styles.portfolio}>Crypto</div>
        </Link>
      </Link>
      <Link className={styles.frame2} to="/5stocks">
        <div className={styles.stocksWrapper}>
          <div className={styles.stocks}>Stocks</div>
        </div>
      </Link>
      <a className={styles.frame3} target="_blank" href="/4login">
        <div className={styles.stocksWrapper}>
          <div className={styles.loginSign}>lOGIN | SIGN UP</div>
        </div>
      </a>
      <div className={styles.homeItem} />
      <div className={styles.homeInner} />
      <div className={styles.rectangleDiv} />
      <div className={styles.homeChild1} />
      <Link className={styles.topCryptocurrencies} to="/2crypto">
        Top Cryptocurrencies
      </Link>
      <img className={styles.rectangleIcon} alt="" src="/rectangle-26@2x.png" />
      <div className={styles.homeChild2} />
      <div className={styles.homeChild3} />
      <div className={styles.homeChild4} />
      <div className={styles.homeChild5} />
      <div className={styles.homeChild6} />
      <div className={styles.homeChild7} />
      <div className={styles.ellipseDiv} />
      <div className={styles.homeChild8} />
      <div className={styles.homeChild9} />
      <div className={styles.homeChild10} />
      <div className={styles.homeChild11} />
      <div className={styles.homeChild12} />
      <a
        className={styles.bitcoinBtcContainer}
        href="https://coinmarketcap.com/currencies/bitcoin/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span>
          <span>{`Bitcoin  `}</span>
          <span className={styles.btc}>{`BTC  |  $34,358.07 `}</span>
        </span>
        <span className={styles.btc}>
          <span>{` `}</span>
        </span>
      </a>
      <a
        className={styles.hederaHbarContainer}
        href="https://coinmarketcap.com/currencies/hedera/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span className={styles.hederaHbar3435807}>
          <span>{`Hedera  `}</span>
          <span className={styles.hbar}>HBAR | $34,358.07</span>
        </span>
        <span className={styles.hbar}>
          <span>{` `}</span>
          <span className={styles.sol}>{` `}</span>
        </span>
      </a>
      <a
        className={styles.solanaSolContainer}
        href="https://coinmarketcap.com/currencies/solona/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span className={styles.xrpXrpCheap}>
          <span>{`Solana  `}</span>
          <span className={styles.sol}>{`SOL   |  $34,358.07 `}</span>
        </span>
        <span className={styles.sol}>
          <span>{` `}</span>
        </span>
      </a>
      <a
        className={styles.xrpXrpContainer}
        href="https://coinmarketcap.com/currencies/ripple/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span className={styles.xrpXrpCheap}>
          <span>{`xRP  `}</span>
          <span className={styles.sol}>{`XRP        |  $34,358.07 `}</span>
        </span>
        <span className={styles.sol}>
          <span>{` `}</span>
        </span>
      </a>
      <a
        className={styles.litecoinLtcContainer}
        href="https://coinmarketcap.com/currencies/litecoin/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span>
          <span>{`Litecoin  `}</span>
          <span className={styles.btc}>{`LTC  |  $3429.07 `}</span>
        </span>
        <span className={styles.btc}>
          <span>{` `}</span>
        </span>
      </a>
      <a
        className={styles.ethereumEthContainer}
        href="https://coinmarketcap.com/currencies/etherium/"
      >
        <span>
          <span className={styles.span6}>{`            `}</span>
          <span>Ethereum ETH</span>
        </span>
        <span className={styles.xrpXrpCheap}> | $1,790.74</span>
      </a>
      <img className={styles.eth1Icon} alt="" src="/eth-1@2x.png" />
      <img className={styles.liteIcon} alt="" src="/lite@2x.png" />
      <img className={styles.btc1Icon} alt="" src="/btc-1@2x.png" />
      <img className={styles.xrpIcon} alt="" src="/xrp@2x.png" />
      <img className={styles.hbarIcon} alt="" src="/hbar@2x.png" />
      <img className={styles.image1Icon} alt="" src="/image-1@2x.png" />
      <img className={styles.homeChild13} alt="" src="/rectangle-26@2x.png" />
      <div className={styles.homeChild14} />
      <div className={styles.homeChild15} />
      <div className={styles.homeChild16} />
      <div className={styles.homeChild17} />
      <div className={styles.homeChild18} />
      <div className={styles.homeChild19} />
      <a
        className={styles.bitcoinBtcContainer1}
        href="https://coinmarketcap.com/currencies/bitcoin/"
        target="_blank"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span>
          <span>{`Bitcoin  `}</span>
          <span className={styles.btc1}>BTC | EXPENSIVE</span>
        </span>
      </a>
      <a
        className={styles.hederaHbarContainer1}
        href="https://coinmarketcap.com/currencies/hedera/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span>
          <span>{`Hedera  `}</span>
          <span className={styles.btc}>HBAR | CHEAP</span>
        </span>
        <span className={styles.btc}>
          <span>{` `}</span>
        </span>
      </a>
      <a
        className={styles.solanaSolContainer1}
        href="https://coinmarketcap.com/currencies/solona/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span>
          <span>{`Solana  `}</span>
          <span className={styles.btc1}>SOL | CHEAP</span>
        </span>
      </a>
      <a
        className={styles.xrpXrpContainer1}
        href="https://coinmarketcap.com/currencies/ripple/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span className={styles.xrpXrpCheap}>
          <span>{`xRP  `}</span>
          <span>XRP | CHEAP</span>
        </span>
      </a>
      <a
        className={styles.litecoinLtcContainer1}
        href="https://coinmarketcap.com/currencies/litecoin/"
      >
        <span>
          <span>{`            `}</span>
        </span>
        <span>
          <span>{`Litecoin  `}</span>
          <span className={styles.btc1}>LTC | EXPENSIVE</span>
        </span>
      </a>
      <a
        className={styles.ethereumEthContainer1}
        href="https://coinmarketcap.com/currencies/etherium/"
      >
        <span>
          <span className={styles.span6}>{`            `}</span>
          <span>Ethereum ETH</span>
        </span>
        <span className={styles.xrpXrpCheap}> | EXPENSIVE</span>
      </a>
      <img className={styles.eth2Icon} alt="" src="/eth-1@2x.png" />
      <img className={styles.liteIcon1} alt="" src="/lite@2x.png" />
      <img className={styles.btc2Icon} alt="" src="/btc-1@2x.png" />
      <img className={styles.xrpIcon1} alt="" src="/xrp@2x.png" />
      <img className={styles.hbarIcon1} alt="" src="/hbar@2x.png" />
      <img className={styles.image2Icon} alt="" src="/image-1@2x.png" />
      <div className={styles.i}>I</div>
      <div className={styles.n}>N</div>
      <div className={styles.v}>V</div>
      <img
        className={styles.appLogoInspiraton8}
        alt=""
        src="/app-logo-inspiraton-8@2x.png"
      />
      <div className={styles.algorithmSays}>Algorithm says...</div>
      <div className={styles.homeChild20} />
      <div className={styles.trending}>Trending</div>
      <div className={styles.homeChild21} />
      <div className={styles.homeChild22} />
      <div className={styles.homeChild23} />
      <img className={styles.image12Icon} alt="" src="/image-5@2x.png" />
      <img className={styles.image13Icon} alt="" src="/image-6@2x.png" />
      <img className={styles.image14Icon} alt="" src="/image-7@2x.png" />
      <img className={styles.image15Icon} alt="" src="/image-8@2x.png" />
      <img className={styles.image16Icon} alt="" src="/image-9@2x.png" />
      <img className={styles.image17Icon} alt="" src="/image-10@2x.png" />
      <div className={styles.homeChild24} />
      <div className={styles.celestiaHasPotential}>
        Celestia has potential to 10X.
      </div>
      <img className={styles.vectorIcon} alt="" src="/vector@2x.png" />
      <div className={styles.bitcoinShouldDump}>
        Bitcoin should dump to 30K!
      </div>
      <img className={styles.vectorIcon1} alt="" src="/vector@2x.png" />
      <div className={styles.avalunchIsGoingContainer}>
        <p className={styles.avalunchIsGoing}>
          Avalunch is going to launch a new IDO .
        </p>
        <p className={styles.avalunchIsGoing}>Price may go higher.</p>
      </div>
      <img className={styles.vectorIcon2} alt="" src="/vector@2x.png" />
      <div className={styles.suggestions}>suggestions</div>
      <img className={styles.lineIcon} alt="" src="/line-30@2x.png" />
      <div className={styles.lineDiv} />
      <div className={styles.lineDiv} />
    </div>
  );
};

export default HOME;
