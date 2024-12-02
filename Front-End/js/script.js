var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate() {
    var username = document.getElementById("uname").value;
    var password = document.getElementById("psw").value;
    if (username == "Admin" && password == "Password") {
        alert("Login successfully");
        window.location = "app.html"; // Redirecting to other page.
        console.log('clicked!')
        return true;
    }
    else {
        attempt--;// Decrementing by one.
        alert("You have" + attempt + " attempts left");
        // Disabling fields after 3 attempts.
        if (attempt == 0) {
            document.getElementById("uname").disabled = true;
            document.getElementById("psw").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}

import React, { useState } from 'react';
import axios from 'axios';


function AddTransaction() {
    const [formData, setFormData] = useState({
        user_id: '',
        amount: '',
        category_id: '',
        description: '',
        date: ''
    });


    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/add_transaction', formData);
            alert('Transaction added successfully!');
        } catch (error) {
            console.error('Error adding transaction:', error);
        }
    };


    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="user_id" placeholder="User ID" onChange={(e) => setFormData({...formData, user_id: e.target.value})} />
            <input type="number" name="amount" placeholder="Amount" onChange={(e) => setFormData({...formData, amount: e.target.value})} />
            <input type="text" name="category_id" placeholder="Category ID" onChange={(e) => setFormData({...formData, category_id: e.target.value})} />
            <textarea name="description" placeholder="Description" onChange={(e) => setFormData({...formData, description: e.target.value})} />
            <input type="date" name="date" onChange={(e) => setFormData({...formData, date: e.target.value})} />
            <button type="submit">Add Transaction</button>
        </form>
    );