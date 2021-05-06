import React, { useState, useEffect } from "react";
import TinderCard from "react-tinder-card";
import './TinderCards.css'
import axios from './axios'

function TinderCards() {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const req = await axios.get("/tinder/cards")

      setPeople(req.data)
    }

    fetchData()
  }, [])

  console.log(people)

  const swiped = (direction, nameToDelete) => {
    console.log(nameToDelete);
    // setLastDirection(direction);
  };

  const outOfFrame = (name) => {
    console.log(name);
  };

  return (
    <div className="tinderCards">
      <div className="cardContainer">
        {people.map((person) => {
          return (
            <TinderCard
              className="swipe"
              key={person.name}
              preventSwipe={["down", "up"]}
              onSwipe={(dir) => swiped(dir, person.name)}
              onCardLeftScreen={() => outOfFrame(person.name)}
            >
              <div
                className="card"
                style={{
                  backgroundImage: `url(${person.imgUrl})`,
                }}
              >
                <h1>{person.name}</h1>
              </div>
            </TinderCard>
          );
        })}
      </div>
    </div>
  );
}

export default TinderCards;
