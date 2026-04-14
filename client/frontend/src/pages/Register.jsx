import { useState } from "react";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/users/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      const data = await res.json();

      if (res.ok) {
  alert("User registered successfully");
  window.location.href = "/";   // 👈 go to login page
} else {
        alert(data.error || "Something went wrong");
      }
    } catch (err) {
      console.error(err);
      alert("Server error");
    }
  };

  return (
    <div>
      <h2>Register</h2>

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <br /><br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <br /><br />

      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
