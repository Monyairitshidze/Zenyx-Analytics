import { useEffect, useState } from "react";
import "./Analysis.css";
import { Bar } from "react-chartjs-2";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend
);

export default function Analysis() {
  const [analyse, setAnalyse] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/analysis")
      .then((data) => data.json())
      .then((res) => setAnalyse(res))
      .catch(() => {
        console.log("Error");
      });
  }, []);

  if (!analyse) {
    return <h2>Loading...</h2>;
  }

  const chartData = {
    labels: analyse.data.map((item) => item.initial),
    datasets: [
      {
        label: "Users by Name Initial",
        data: analyse.data.map((item) => item.count),
      },
    ],
  };

  return (
    <div className="analysis-container">
      <h2>User Registration Analysis</h2>
      <Bar data={chartData} />
    </div>
  );
}

