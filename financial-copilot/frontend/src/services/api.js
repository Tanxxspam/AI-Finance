import axios from "axios";

export const askQuestion = async (query) => {
  const response = await axios.post(
    "http://127.0.0.1:8000/query",
    { query }
  );

  return response.data;
};