import React from "react";
import "./SwipeButton.css";
import ReplayIcon from "@material-ui/icons/Replay";
import CloseIcon from "@material-ui/icons/Close";
import StarRateIcon from "@material-ui/icons/StarRate";
import FlashOnIcon from "@material-ui/icons/FlashOn";
import FavoriteIcon from "@material-ui/icons/Favorite";
import { IconButton } from "@material-ui/core";

function SwipeButton() {
  return (
    <div className="swipeButton" style={{
        position: "fixed",
        bottom: "10vh",
        display: "flex",
        width: "100%",
        justifyContent: "space-evenly"
    }}>
      <IconButton>
        <ReplayIcon />
      </IconButton>
      <IconButton>
        <CloseIcon />
      </IconButton>
      <IconButton>
        <StarRateIcon />
      </IconButton>
      <IconButton>
        <FavoriteIcon />
      </IconButton>
      <IconButton>
        <FlashOnIcon />
      </IconButton>
    </div>
  );
}

export default SwipeButton;
