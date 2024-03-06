import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {useLocation, useNavigate } from 'react-router-dom';

import './Home.css';

const Home = () => {
  const location = useLocation();
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);
  const navigate = useNavigate();
   
  // console.log(location)
  const answerChangeHandler = (event) => {
    setAnswers(event.target.value);
  }
  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/question/');
        // console.log(response.data);
        setQuestions(response.data.data); 
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchQuestions();
  }, []);

  const handleLogout = () => {
    localStorage.clear();
    navigate('/');
  };


  const clickhandler = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.get('http://127.0.0.1:8000/api/question/');
      setQuestions(response.data.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
    // console.log(questions[0])
    const requestData={
      user_id:location.state.user_id,
      question_id:questions[0].id,
      answer:answers,
    };
    console.log(requestData)
   
    try {
      const response2 = await axios.post('http://127.0.0.1:8000/api/answer/', requestData);
      if(response2.data===400){
        alert(response2.data.error)
      }
    }catch (error) {
      if (error.response.status === 400) {
        alert('Alrready attempted 5 questions ');
        navigate('/')
      } 
      else {
        console.error('Error posting data:', error);
      }
    setAnswers('')
  };
}


  return (
    <div>
      <h1>Home Page</h1>
      <button onClick={handleLogout}>Logout</button>
    
        <>
          <h2>Questions</h2>
          <form >
            <div className="question-container">
              {questions.map((question, index) => (
                <div className="question" key={index}>
                  <label>{question.question}</label>
                  <input
                    type="text"
                    value={answers}
                    placeholder="Answer"
                    onChange={answerChangeHandler}
                    required
                  />
                </div>
              ))}
            </div>
            <button type="submit" onClick={clickhandler}>Submit Answers</button>
          </form>
        </>
    </div>
  );
};

export default Home;
