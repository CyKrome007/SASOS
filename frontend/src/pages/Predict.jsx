import React, { useState } from "react";
import { Box, Button, TextField, Typography, Container, Paper, Grid, CircularProgress } from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import axios from "axios";
import { server } from "../constants/config.js";

// Create a green light/dark theme
const theme = createTheme({
  palette: {
    mode: "light", // You can toggle between "light" or "dark" for dark mode
    primary: {
      main: "#4caf50", // Dark Green
    },
    secondary: {
      main: "#81c784", // Light Green
    },
  },
});

const Predict = () => {

  //   const [N, setN] = useState("");
  //   const [P, setP] = useState("");
  //   const [K, setK] = useState("");
  //   const [temperature, setTemperature] = useState("");
  //   const [humidity, setHumidity] = useState("");
  //   const [ph, setPh] = useState("");
  //   const [rainfall, setRainfall] = useState("");
  //
  // const [formData, setFormData] = useState({
  //   N: N.value,
  //   P: P.value,
  //   K: K.value,
  //   temperature: temperature.value,
  //   humidity: humidity.value,
  //   ph: ph.value,
  //   rainfall: rainfall.value,
  // });

  const [formData, setFormData] = useState({
    N: 90,
    P: 42,
    K: 43,
    temperature: 20.87,
    humidity: 92.80,
    ph: 6.50,
    rainfall: 202.93
  })

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      axios.post(
          `${server}/predict`,
          formData,
          {
            headers: {
              'Content-Type': 'application/json',
              'WithCredentials': 'true'
            },
            withCredentials: 'true',
          }
      ).then(response => {
        setResult(response.data.message); // Assuming the result is in response.data
        console.log(response)
        setLoading(false);
      }).catch(error => {
        console.log(error)
        setLoading(false);
      })

        // const result = await fetch(`${server}/predict`, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify(formData),
        //     credentials: 'include',
        // })
        //
        // console.log(result)

    } catch (error) {
      console.error("Error during the API call", error);
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="sm" sx={{ paddingTop: 5 }}>
        <Paper elevation={3} sx={{ padding: 3, borderRadius: 2 }}>
          <Typography variant="h4" align="center" color="primary" gutterBottom>
            Crop Prediction Form
          </Typography>
          <form onSubmit={handleSubmit}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Nitrogen (N)"
                  variant="outlined"
                  fullWidth
                  name="N"
                  value={formData.N}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Phosphorus (P)"
                  variant="outlined"
                  fullWidth
                  name="P"
                  value={formData.P}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Potassium (K)"
                  variant="outlined"
                  fullWidth
                  name="K"
                  value={formData.K}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Temperature (°C)"
                  variant="outlined"
                  fullWidth
                  name="temperature"
                  value={formData.temperature}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Humidity (%)"
                  variant="outlined"
                  fullWidth
                  name="humidity"
                  value={formData.humidity}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="pH"
                  variant="outlined"
                  fullWidth
                  name="ph"
                  value={formData.ph}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Rainfall (mm)"
                  variant="outlined"
                  fullWidth
                  name="rainfall"
                  value={formData.rainfall}
                  onChange={handleChange}
                  type="number"
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <Box display="flex" justifyContent="center" marginTop={2}>
                  <Button
                    type="submit"
                    variant="contained"
                    color="primary"
                    size="large"
                    disabled={loading}
                  >
                    {loading ? <CircularProgress size={24} color="inherit" /> : "Predict"}
                  </Button>
                </Box>
              </Grid>
            </Grid>
          </form>
          {result && (
            <Box marginTop={3} display="flex" justifyContent="center">
              <Typography variant="h6" color="secondary">
                {result}
              </Typography>
            </Box>
          )}
        </Paper>
      </Container>
    </ThemeProvider>
  );
};

export default Predict;
