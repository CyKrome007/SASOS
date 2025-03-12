import { configureStore } from "@reduxjs/toolkit";
import authSlice from "./reducers/auth.js";
import miscSlice from "./reducers/misc.js";

const store = configureStore({
    reducer: {
        [authSlice.name]: authSlice.reducer,
        [miscSlice.name]: miscSlice.reducer,
    }
});

export default store;