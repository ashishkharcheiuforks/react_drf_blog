import {FETCH_POST} from "../actions";

export default (state=null, action) => {
    switch (action.type) {
        case FETCH_POST:
            return action.payload;
        default:
            return state;
    }
};
