import React, { useState } from "react";

function EventCard({
  handleDelete,
  event,
  onUpdate,
  handlePostStatus,
  volunteers,
}) {
  const [eventStatus, setEventStatus] = useState(true);
  const [form, setForm] = useState({
    title: "",
    description: "",
  });
  const [selectedVolunteer, setSelectedVolunteer] = useState("");

  function handleAddVolunteer() {
    if (selectedVolunteer) {
      const newRegistration = {
        account_id: selectedVolunteer,
        opportunity_id: event.id,
      };
      fetch("/registrations", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newRegistration),
      })
        .then((r) => r.json())
        .then(handlePostStatus);
    } else {
      console.log("No volunteer selected");
    }
  }

  function removeSignup(id) {
    fetch(`/registrations/${id}`, {
      method: "DELETE",
    }).then(handlePostStatus);
  }

  function handleEventStatus() {
    setForm(event);
    setEventStatus(!eventStatus);
  }

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  function handleEventUpdate() {
    fetch(`/events/${event.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    })
      .then((r) => r.json())
      .then((updatedEvent) => onUpdate(updatedEvent));
  }

  function handleEventDelete(event) {
    console.log(event);
    fetch(`/events/${event.id}`, {
      method: "DELETE",
    });
    handleDelete(event);
  }

  const volunteerList =
    Array.isArray(event.registrations) &&
    event.registrations.map((registration) => (
      <div className="list-group">
        <li className="list-group-item">
          {registration.account?.name}
          <button
            id="deleteVolunteerBtn"
            className="btn btn-secondary"
            onClick={() => removeSignup(registration.id)}
          >
            X
          </button>
        </li>
      </div>
    ));

  const volunteerDropDown = (
    <>
      <select
        className="btn btn-secondary dropdown-toggle"
        value={selectedVolunteer}
        onChange={(e) => setSelectedVolunteer(e.target.value)}
      >
        <option className="dropdown-item">--Select a Volunteer--</option>
        {volunteers.map((volunteer) => (
          <option className="dropdown-item" value={volunteer.id}>
            {volunteer.name}
          </option>
        ))}
      </select>
      <button className="btn btn-primary" onClick={handleAddVolunteer}>
        Add Volunteer
      </button>
    </>
  );

  // ...

return (
  <div>
    <div className="card">
      {eventStatus ? (
        <div className="card-body">
          <h3 className="card-title">{event.title}</h3>
          <p className="card-text">{event.description}</p>
          <div className="card-buttons-container">
            <button className="btn btn-primary" onClick={handleEventStatus}>
              Edit Event
            </button>
            <button
              className="btn btn-secondary"
              onClick={() => handleEventDelete(event)}
            >
              Delete Event
            </button>
          </div>
          {volunteerList.length > 0 ? (
            <>
              {volunteerDropDown}
              <h5 className="card-header">Volunteers</h5>
            </>
          ) : volunteerDropDown}
          {volunteerList}
        </div>
      ) : (
        <form onSubmit={handleEventUpdate} className="card-body">
          <input
            type="text"
            value={form.title}
            onChange={handleChange}
            name="title"
            className="form-control card-title"
          />
          <input
            type="text"
            value={form.description}
            onChange={handleChange}
            name="description"
            className="form-control card-text"
          />
          <button className="btn btn-primary" type="submit">
            Submit
          </button>
          <button className="btn btn-danger" onClick={handleEventStatus}>
            x
          </button>
        </form>
      )}
    </div>
  </div>
 );
 
}

export default EventCard;
