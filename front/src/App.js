import React, { useMemo, useState, useEffect } from 'react';
import './App.css';
import TableContainer from './Table';
import "bootstrap/dist/css/bootstrap.min.css"
import { SelectColumnFilter } from './filters';

function App() {

  const columns = useMemo(
      () => [
        {
          Header: "Runner Table",
          columns: [
            {
              Header: "Age Group",
              accessor: "age_group",
              Filter: SelectColumnFilter,
              filter: "equals",
              disableSortBy: true
            },
            {
              Header: "Name",
              accessor: "username",
              disableFilters: true,
              disableSortBy: true
            },
            {
              Header: "Age",
              accessor: "age",
              disableFilters: true
            },
            {
              Header: "Gender",
              accessor: "gender",
              disableFilters: true
            },
            {
              Header: "Total Time (min)",
              accessor: "total_time",
              disableFilters: true
            },
            {
              Header: "Distance (m)",
              accessor: "distance",
              disableFilters: true
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
              sortType: 'basic',
              disableFilters: true
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
  <TableContainer columns={columns} data={data} />
    </div>
  );
}

export default App;
