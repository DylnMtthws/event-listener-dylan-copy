import React from "react";

function VolunteerCard({ name, email, registrations }) {
  return (
    <div className="card">
      <div className="card-body">
        <h3 className="card-title">{name}</h3>
        <p className="card-header">{email}</p>
        {registrations.map((registration) => (
          <ul>
            <li className="card-text">{registration.opportunity.title}
            <ul className="card-text">{registration.opportunity.description}</ul>
            </li>
          </ul>
        ))}
      </div>
    </div>
  );
}

export default VolunteerCard;
