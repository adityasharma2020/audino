import axios from "axios";
import authHeader from "./auth-header";
import chunkUpload from "../functions/chunkUpload";
import { toast } from "react-hot-toast";

const BASE_URL = process.env.REACT_APP_BACKEND_URL;


export const fetchJobsApi = async (data) => {
  try {
    const res = await axios.get(BASE_URL + "/jobs", {
      params: {
        org: data?.org,
        page: data?.page,
        page_size: data?.page_size,
        filter: data?.filter,
        search: data?.searchValue,
      },
      headers: { ...authHeader() },
    });
    return res.data;
  } catch (e) {
    throw Error(e.response?.data?.msg ?? "Something went wrong");
  }
};

export const fetchJobDetailApi = async (data) => {
  try {
    const res = await axios.get(BASE_URL + "/jobs/"+ data.jobId, {
      params: {
        org: data?.org,
        // page: data?.page,
        // page_size: data?.page_size,
        // filter: data?.filter,
        // search: data?.searchValue,
      },
      headers: { ...authHeader() },
    });
    return res.data;
  } catch (e) {
    throw Error(e.response?.data?.msg ?? "Something went wrong");
  }
};


export const fetchAnnotationDataApi = async (data) => {
  try {
    const res = await axios.get(BASE_URL + "/tasks/" + data.id + "/data", {
      params: {
        org: data?.org,
      },
      headers: { ...authHeader() },
    });
    return res.data;
  } catch (e) {
    throw Error(e.response?.data?.msg ?? "Something went wrong");
  }
};

export const fetchAllAnnotationApi = async (data) => {
  try {
    const res = await axios.get(BASE_URL + "/jobs/" + data.id + "/annotation", {
      params: {
        org: data?.org,
      },
      headers: { ...authHeader() },
    });
    return res.data;
  } catch (e) {
    throw Error(e.response?.data?.msg ?? "Something went wrong");
  }
};

export const postAnnotationApi = async ({data, jobId}) => {
  try {
    const res = await axios.post(
      BASE_URL + "/jobs/" + jobId + "/annotation",
      data,
      {
        params: {
          org: data?.org,
        },
        headers: { ...authHeader() },
      }
    );
    return res.data;
  } catch (e) {
    throw Error(e.response?.data?.msg ?? "Something went wrong");
  }
};

export const getAllAnnotationApi = async ({data, jobId}) => {
  try {
    const res = await axios.get(BASE_URL + "/jobs/" + jobId + "/annotation", {
      params: {
        org: data?.org,
      },
      headers: { ...authHeader() },
    });
    return res.data;
  } catch (e) {
    throw Error(e.response?.data?.msg ?? "Something went wrong");
  }
};

