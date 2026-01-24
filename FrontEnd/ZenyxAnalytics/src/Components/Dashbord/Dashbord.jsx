import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Dashbord.css";

export default function Dashbord() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/me")
      .then((response) => response.json())
      .then((data) => {
        setUser(data);
      })
      .catch((error) => {
        console.error("Error fetching user:", error);
      });
  }, []);

  if (!user) {
    return <h2>Loading...</h2>;
  }

  return (
    <div className="dashbord-cover">
      <div className="dashbord">
        <div className="button-cover">
          <ul className="button">
            <li><h3>Dashboard</h3></li>

            <li>
              <button className="home">Home</button>
            </li>

            <li>
              <button className="records">Records</button>
            </li>

            <li>
              <button
                className="analyse"
                onClick={() => navigate("/analysis")}
              >
                Analyse
              </button>
            </li>

            <li>
              <button className="logout">Logout</button>
            </li>
          </ul>
        </div>

        <div className="left-side-cover">
          <div className="left-side">
            <h1>Welcome Back</h1>
            <h2>Your details are</h2>

            <table>
              <thead>
                <tr>
                  <th>Field</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Full Name</td>
                  <td>{user.fullName}</td>
                </tr>
                <tr>
                  <td>Username</td>
                  <td>{user.username}</td>
                </tr>
                <tr>
                  <td>Email</td>
                  <td>{user.email}</td>
                </tr>
                <tr>
                  <td>Password</td>
                  <td>{user.password}</td>
                </tr>
                <tr>
                  <td>Confirm Password</td>
                  <td>{user.confirmPassword}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="image-cover">
            <img
              src="images/images3.jpg"
              alt="analyzing-image"
              className="analyze"
            />
          </div>
        </div>
      </div>
    </div>
  );
}
