import React from "react";
import VolunteerCard from "./VolunteerCard";

const ManageVolunteers = ({ volunteers }) => {
  return (
    <>
      <h1 className="page-header">Manage Volunteers</h1>
      <div className="container-fluid overflow-auto">
        <div className="row">
          {volunteers.map((volunteer) => (
            <div className="card-container">
              <VolunteerCard
                key={volunteer.id}
                name={volunteer.name}
                email={volunteer.email}
                registrations={volunteer.registrations}
              />
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default ManageVolunteers;
