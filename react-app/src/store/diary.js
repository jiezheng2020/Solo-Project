const GET_DIARIES = "diary/GET_DIARIES";
const CREATE_DIARY = "diary/CREATE_DIARY";
const CREATE_FOODENTRY = "food/CREATE_FOODENTRY";
const EDIT_FOODENTRY = "food/EDIT_FOODENTRY";

const getDiaries = (diary) => {
  return {
    type: GET_DIARIES,
    diary,
  };
};

const createDiary = (diary) => {
  return {
    type: CREATE_DIARY,
    diary,
  };
};

const createFoodEntries = (food) => {
  return {
    type: CREATE_FOODENTRY,
    food,
  };
};

const editFoodEntries = (food) => {
  return {
    type: EDIT_FOODENTRY,
    food,
  };
};

export const fetchDiaries = (currDate) => async (dispatch) => {
  const res = await fetch("/api/diary/");

  if (res.ok) {
    const diary = await res.json();
    const userDiary = diary.filter((diaries) =>
      diaries.date.includes(currDate)
    );

    dispatch(getDiaries(userDiary));
    return userDiary;
  }
};

export const createDiaries = (currDate) => async (dispatch) => {
  const res = await fetch("/api/diary/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ currDate }),
  });

  if (res.ok) {
    const diary = await res.json();
    dispatch(createDiary(diary));
    return diary;
  }
};

export const createFoodEntry =
  ({ foodId, diaryId, mealType, totalCalories }) =>
  async (dispatch) => {
    const res = await fetch("/api/food/entry", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ foodId, diaryId, mealType, totalCalories }),
    });

    if (res.ok) {
      const food = await res.json();
      dispatch(createFoodEntries(food));
    }
  };

export const editFoodEntry =
  ({ foodId, totalCalories }) =>
  async (dispatch) => {
    const res = await fetch("/api/food/entry", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ foodId, totalCalories }),
    });

    if (res.ok) {
      const food = await res.json();
      console.log(food);
      dispatch(editFoodEntries(food));
    }
  };

const initialState = [];
export default function reducer(state = initialState, action) {
  let newState = [];

  switch (action.type) {
    case GET_DIARIES: {
      return action.diary;
    }

    case CREATE_DIARY: {
      newState = [...state, action.diary];

      return newState;
    }
    case CREATE_FOODENTRY: {
      newState = [...state];
      newState[0].diaryFoods.push(action.food);
      return newState;
    }
    case EDIT_FOODENTRY: {
      let index = 0;
      newState = [...state];
      newState[0].diaryFoods.forEach((entry, i) => {
        if (entry.id == action.food.id) {
          index = i;
        }
      });

      newState[0].diaryFoods.splice(index, 1, action.food);
      return newState;
    }

    default:
      return state;
  }
}
