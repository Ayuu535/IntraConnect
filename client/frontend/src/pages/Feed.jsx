import { useEffect, useState } from "react";
import API from "../api/axios";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      const res = await API.get("/posts/");
      setPosts(res.data.results);
    };
    fetchPosts();
  }, []);

  return (
    <div>
      <h2>Feed</h2>
      {posts.map((post) => (
        <div key={post.id}>
          <p>{post.text}</p>
          <p>Votes: {post.vote_score}</p>
          <p>Comments: {post.comment_count}</p>
        </div>
      ))}
    </div>
  );
}