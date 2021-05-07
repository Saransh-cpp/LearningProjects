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
        src="https://www.flaticon.com/svg/vstatic/svg/732/732251.svg?token=exp=1620323226~hmac=d939d6d9f8eb9b4d4fdacc9e601f83a4"
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
