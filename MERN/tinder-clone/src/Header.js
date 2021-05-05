import React from "react";
import PersonIcon from "@material-ui/icons/Person";
import { IconButton } from "@material-ui/core";
import "./Header.css";
import { ForumRounded } from "@material-ui/icons";

function Header() {
  return (
    <div className="header">
      <IconButton className="headerIcons">
        <PersonIcon />
      </IconButton>

      <img
        className="header_logo"
        src="https://www.flaticon.com/svg/vstatic/svg/408/408739.svg?token=exp=1620249207~hmac=cd695fd574c903b400be2e982a247cec"
        alt="tinder-logo"
        height="20px"
      />

      <IconButton className="headerIcons">
        <ForumRounded />
      </IconButton>
    </div>
  );
}

export default Header;
