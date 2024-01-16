import React, { useState } from 'react';

const EventForm = ({ addEvent, handlePostStatus }) => {
  const [form, setForm] = useState({
    id: '',
    title: '',
    description: '',
    start_date: '',
    end_date: '',
    // creator_id: '',
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    console.log(form)
    e.preventDefault();
    fetch("/events", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      })
      .then(r => r.json())
      .then(newEvent => {
        addEvent(newEvent)
        handlePostStatus()
      })
      .then(setForm({
        // id: '',
        title: '',
        description: '',
        start_date: '',
        end_date: '',
        // creator_id: '',
      }))
  };

  return (
    <form className='event-form'onSubmit={handleSubmit}>
      <label>
        Title:
        <input type="text" name="title"  value={form.title} onChange={handleChange} required  />
      </label>
      <label>
        Description:
        <textarea name="description"  value={form.description} onChange={handleChange} required />
      </label>
      <label>
        Start Date:
        <input type="date" name="start_date"  value={form.start_date} onChange={handleChange} required />
      </label>
      <label>
        End Date:
        <input type="date" name="end_date"  value={form.end_date} onChange={handleChange} required />
      </label>
      {/* <label>
        Creator ID:
        <input type="text" name="creator_id" value={form.creator_id} onChange={handleChange} required />
      </label> */}
      <button type="submit" className='submit1'>Submit</button>
    </form>
  );
};

export default EventForm;
