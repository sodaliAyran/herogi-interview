import React, { useMemo, useState, useEffect } from 'react';
import './App.css';
import Table from './Table';

function App() {

  const columns = useMemo(
      () => [
        {
          Header: "Runner Table",
          columns: [
            {
              Header: "Name",
              accessor: "username"
            },
            {
              Header: "Age",
              accessor: "age"
            },
            {
              Header: "Gender",
              accessor: "gender"
            },
            {
              Header: "Total Time (min)",
              accessor: "total_time"
            },
            {
              Header: "Distance (m)",
              accessor: "distance"
            },
            {
              Header: "Average Pace (min/km)",
              accessor: d => Number(d.average_pace).toFixed(2),
              Cell: ({cell: { value } }) => {
                const pace = Math.round(value * 100)/100;
                return(
                  <>
                  {`${pace}`}
                  </>
                );
              },
              sortType: 'basic'
            },
          ]
        },
      ],
      []
    );

  const [data, setData] = useState([]);

  useEffect(() => {
    (async () => {
      const response = await fetch("http://localhost:5000/get_values");
      const j = await response.json()
      setData(j["result"]);
    })();
  }, []);

  return (
    <div className="App">
      <Table columns={columns} data={data} />
    </div>
  );
}

export default App;
