import { useState } from "react";
import API from "../api/axios";

export default function Login() {
  const [data, setData] = useState({ username: "", password: "" });

  const handleLogin = async () => {
    try {
      const res = await API.post("/users/login/", data);
      localStorage.setItem("token", res.data.access);
      alert("Login success");
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        placeholder="username"
        onChange={(e) => setData({ ...data, username: e.target.value })}
      />
      <input
        placeholder="password"
        type="password"
        onChange={(e) => setData({ ...data, password: e.target.value })}
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}