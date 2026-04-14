import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";

export default function Feed() {
  const [posts, setPosts] = useState([]);
  const [text, setText] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    if (!localStorage.getItem("access")) {
      navigate("/");
    }
  }, []);

  const fetchPosts = async () => {
    const res = await API.get("posts/");
    setPosts(Array.isArray(res.data) ? res.data : res.data.results);


  };

  useEffect(() => {
    fetchPosts();
  }, []);

  const createPost = async () => {
  try {
    await API.post("posts/", { text });

    setText("");
    fetchPosts();
  } catch (err) {
    console.log(err.response?.data);
  }
};


  const vote = async (postId, value) => {
  try {
    await API.post("votes/", {   // ✅ FIXED URL
      post: postId,              // ✅ send post id
      vote_type: value,
    });

    // refresh posts from backend (BEST way)
    fetchPosts();

  } catch (err) {
    console.error(err.response?.data || err);
  }
  
};


  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🔥 Feed</h2>

      {/* CREATE POST */}
      <div style={styles.postBox}>
        <textarea
          style={styles.textarea}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="What's on your mind?"
        />
        <button style={styles.postBtn} onClick={createPost}>
          Post
        </button>
      </div>

      {/* POSTS */}
      {posts.map((post) => (
        <div key={post.id} style={styles.card}>
          <div style={styles.header}>
            <span style={styles.username}>
              👤 {post.user}
            </span>
          </div>

          <p style={styles.text}>{post.text}</p>

          <div style={styles.actions}>
            <button
              style={styles.up}
              onClick={() => vote(post.id, 1)}
            >
              ⬆ Upvote
            </button>

            <button
              style={styles.down}
              onClick={() => vote(post.id, -1)}
            >
              ⬇ Downvote
            </button>

            <span style={styles.score}>
              ⭐ {post.vote_score || 0}
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "600px",
    margin: "auto",
    padding: "20px",
    fontFamily: "Arial",
  },

  title: {
    textAlign: "center",
    marginBottom: "20px",
  },

  postBox: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    marginBottom: "20px",
  },

  textarea: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    minHeight: "60px",
  },

  postBtn: {
    padding: "8px",
    background: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
  },

  card: {
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "15px",
    marginBottom: "15px",
    background: "#fff",
  },

  header: {
    marginBottom: "8px",
    fontSize: "14px",
    color: "#555",
  },

  username: {
    fontWeight: "bold",
  },

  text: {
    fontSize: "16px",
    marginBottom: "10px",
  },

  actions: {
    display: "flex",
    gap: "10px",
    alignItems: "center",
  },

  up: {
    background: "#e6f4ea",
    border: "none",
    padding: "6px 10px",
    borderRadius: "6px",
    cursor: "pointer",
  },

  down: {
    background: "#fdecea",
    border: "none",
    padding: "6px 10px",
    borderRadius: "6px",
    cursor: "pointer",
  },

  score: {
    marginLeft: "auto",
    fontWeight: "bold",
  },
};
