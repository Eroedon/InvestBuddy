import { TextField, InputAdornment, Icon, IconButton } from "@mui/material";
import { Link } from "react-router-dom";
import styles from "./LogIn.module.css";

const LogIn = () => {
  return (
    <div className={styles.logIn}>
      <div className={styles.logIn1}>Log In</div>
      <img className={styles.logInChild} alt="" src="/line-1@2x.png" />
      <TextField
        className={styles.logInItem}
        color="primary"
        label="E-mail"
        variant="filled"
      />
      <TextField
        className={styles.logInItem}
        color="primary"
        label="password"
        variant="filled"
      />
      <div className={styles.forgotYourPasswordContainer}>
        <span className={styles.forgotYourPasswordContainer1}>
          <span>{`Forgot your password ? Click `}</span>
          <span className={styles.hereToReset}>here to reset.</span>
        </span>
      </div>
      <div className={styles.or}>
        <div className={styles.logInWith}>{` Log In with `}</div>
        <img className={styles.google1Icon} alt="" src="/google-1@2x.png" />
      </div>
      <Link className={styles.logInWrapper} to="/1home">
        <div className={styles.logIn2}>Log In</div>
      </Link>
    </div>
  );
};

export default LogIn;
