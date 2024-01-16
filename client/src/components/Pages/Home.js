import React, { useState } from "react";

const Home = () => {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    name: "",
    email: "",
    role: "",
  });
  const [formKey, setFormKey] = useState(Date.now());

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("/volunteers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then(() => {
        setFormKey(Date.now());
      })
      .then(() => toggleForm())
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div className="home">
      <div className="homeP">
        <h2>Connecting volunteers, creating change</h2>
        <p>
          New here?{" "}
          <button className="btn btn-secondary" onClick={toggleForm}>
            Create an Account
          </button>
        </p>
        {showForm && (
        <form
          className="toggle-create-account"
          key={formKey}
          onSubmit={handleSubmit}
        >
          <label>
            Username:
            <input type="text" name="username" onChange={handleChange} />
          </label>
          <label>
            Password:
            <input type="password" name="password" onChange={handleChange} />
          </label>
          <label>
            Name:
            <input type="text" name="name" onChange={handleChange} />
          </label>
          <label>
            Email:
            <input type="email" name="email" onChange={handleChange} />
          </label>
          <label>
            Role:
            <select name="role" onChange={handleChange}>
              <option value="">Select a role</option>
              <option value="Admin">Admin</option>
              <option value="Volunteer">Volunteer</option>
            </select>
          </label>
          <input type="submit" value="Submit" />
        </form>
      )}
        <div className="image-container">
          {/* <img
            className="overlay-image1"
            src="https://source.unsplash.com/random/800x600?event"
            alt="Community Service Event"
          />
          <img
            className="overlay-image2"
            src="https://source.unsplash.com/random/800x600?volunteer"
            alt="Community Service Event"
          />
          <img
            className="overlay-image3"
            src="https://source.unsplash.com/random/800x600?adminstration"
            alt="Community Service Event"
          />
          <img
            className="overlay-image4"
            src="https://source.unsplash.com/random/800x600?manage"
            alt="Community Service Event"
          /> */}
        </div>
      </div>
    </div>
  );
};

export default Home;
