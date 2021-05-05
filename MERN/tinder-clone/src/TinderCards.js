import React, { setState } from 'react'
import TinderCard from 'react-tinder-card'

function TinderCards() {

    const [people, setPeople] = setState([
        {
            name: "Elon Musk",
            url: "https://upload.wikimedia.org/wikipedia/commons/8/85/Elon_Musk_Royal_Society_%28crop1%29.jpg"
        },
        {
            name: "Jeff Bezos",
            url: "https://specials-images.forbesimg.com/imageserve/5f469ea85cc82fc8d6083f05/960x0.jpg?fit=scale"
        }
    ])
    return (
        <div className="tinderCards">
            <div>
                {
                    people.map((person) => {
                        <TinderCard>

                        </TinderCard>
                    })
                }
            </div>
        </div>
    )
}

export default TinderCards
