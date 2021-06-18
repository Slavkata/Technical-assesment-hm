import axios from "axios";

const baseDomain = process.env.API;
const baseURL = `${baseDomain}`;

export default axios.create({
    baseURL,
    headers: {
    },
});