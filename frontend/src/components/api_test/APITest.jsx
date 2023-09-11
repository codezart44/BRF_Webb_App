import React from "react";
import { useState, useEffect } from "react";

const APITest = () => {

    // param for API response, init to null
    const [getResponse, setGetResponse] = useState('no get response');
    const [postResponse, setPostResponse] = useState('no post response');
    const [paramResponse, setParamResponse] = useState('no param response');

    // effect when mounting component. Dependencies empty (no triggers)
    useEffect(() => {
        fetch('http://127.0.0.1:5000/test/ping')
            .then(response => response.text())
            .then(response => setGetResponse(response))
            .catch(error => console.error('Error with ping', error));
    }, []);

    useEffect(() => {
        const postData = { content: ['Hi Mom!', 'Hi Dad!'] };
        fetch('http://127.0.0.1:5000/test/echo', 
            {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(postData)
            })
            .then(response => response.text())
            .then(response => setPostResponse(response))
            .catch(error => console.error('Error with echo', error));
    }, []);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/test/echo/1234')
            .then(response => response.text())
            .then(response => setParamResponse(response))
            .catch(error => console.error('Error with param', error));
    }, []);


    return (
        <>
        {getResponse}
        <br />
        {postResponse}
        <br />
        {paramResponse}
        </>
    );
};

export default APITest;
