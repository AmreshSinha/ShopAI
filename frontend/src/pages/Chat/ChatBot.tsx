import React, { useEffect } from "react";
import styled from "styled-components";
import axios from "axios";
import { MdPerson } from "react-icons/md";
import { GoHubot } from "react-icons/go";
import { PiPaperPlaneRightFill, PiShuffle } from "react-icons/pi";
import { CircularProgress } from "@mui/material";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";

type ChatBotProps = {
  queryAsked: string;
  userPref: {
    age: number;
    gender: string;
    extra: string;
  };
};

export default function ChatBot<ChatBotProps>({ queryAsked, userPref }) {
  const chatInputRef = React.useRef<HTMLInputElement>(null);

  // Local query asked in ChatBot Page
  const [localQueryAsked, setLocalQueryAsked] = React.useState();

  // Tracking First API call
  const [isFirstCall, setIsFirstCall] = React.useState(true);

  // Storing the list of the conversation
  const [response, setResponse] = React.useState<
    Array<{ role: string; response: any }>
  >([{ role: "user", response: queryAsked }]);
  console.log(queryAsked);
  console.log(userPref);

  // Date in the format of "23 august"
  const monthNames = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
  ];

  // Get the current date
  const currentDate = new Date();

  // Extract day and month
  const day = currentDate.getDate();
  const month = monthNames[currentDate.getMonth()];

  // Form the desired format
  const dateMonth = `${day} ${month}`;

  useEffect(() => {
    // Remove history before running the query
    axios.get("http://localhost:8000/clear").then((res) => {
      // First Query Call
      axios
        .get(`http://localhost:8000/items/${queryAsked}`, {
          params: {
            age: userPref.age,
            location: userPref.state,
            gender: userPref.age.toLowerCase(),
            user_instructions: userPref.extra,
            curr_date: dateMonth,
          },
        })
        .then((res) => {
          if (res.data) {
            setResponse((prevResponses) => {
              setIsFirstCall(false);
              return [...prevResponses, { role: "bot", response: res.data }];
            });
          }
        });
    });
  }, []);

  useEffect(() => {
    if (localQueryAsked) {
      axios
        .get(`http://localhost:8000/items/${localQueryAsked}`, {
          params: {
            age: userPref.age,
            location: userPref.state,
            gender: userPref.age.toLowerCase(),
            user_instructions: userPref.extra,
            curr_date: dateMonth,
          },
        })
        .then((res) => {
          if (res.data) {
            setResponse((prevResponses) => {
              setIsFirstCall(false);
              return [...prevResponses, { role: "bot", response: res.data }];
            });
          }
        });
    }
  }, [localQueryAsked]);

  console.log(response);

  if (isFirstCall)
    return (
      <div
        style={{
          color: "#fff",
          padding: "6rem",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <CircularProgress />
      </div>
    );

  return (
    <ChatBotWrapper>
      <ChatList>
        {response?.map((res) =>
          res.role === "user" ? (
            <UserMessage message={res.response} />
          ) : (
            <BotMessage message={res.response} setResponse={setResponse} />
          )
        )}
      </ChatList>
      <form
        className="input"
        onSubmit={(e) => {
          e.preventDefault();
          const formData = new FormData(e.currentTarget);
          const data = Object.fromEntries(formData.entries());
          setResponse((prevResponses) => [
            ...prevResponses,
            { role: "user", response: data.query },
          ]);
          setLocalQueryAsked(data.query as string);
          chatInputRef.current!.value = "";
          if (localQueryAsked) {
            axios
              .get(`http://localhost:8000/items/${localQueryAsked}`, {
                params: {
                  age: userPref.age,
                  location: userPref.state,
                  gender: userPref.age.toLowerCase(),
                  user_instructions: userPref.extra,
                  curr_date: dateMonth,
                },
              })
              .then((res) => {
                if (res.data) {
                  setResponse((prevResponses) => {
                    setIsFirstCall(false);
                    return [
                      ...prevResponses,
                      { role: "bot", response: res.data },
                    ];
                  });
                }
              });
          }
        }}
      >
        <input
          ref={chatInputRef}
          type="text"
          name="query"
          id="query"
          placeholder="What Outfit are you looking for today?"
          required
        />
        <button>
          <PiPaperPlaneRightFill />
        </button>
      </form>
    </ChatBotWrapper>
  );
}

type UserMessageProps = {
  message: string;
};

function UserMessage<UserMessageProps>({ message }) {
  return (
    <div
      style={{
        width: "100%",
        display: "flex",
        justifyContent: "flex-end",
        flexWrap: "wrap",
      }}
    >
      <div style={{ display: "flex", alignItems: "flex-end", gap: "4px" }}>
        <div className="message-wrapper">
          <p>{message}</p>
        </div>
        <div
          style={{
            width: "24px",
            height: "24px",
            borderRadius: "50%",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            background: "#5F5CD5",
          }}
        >
          <MdPerson color="white" />
        </div>
      </div>
    </div>
  );
}

type BotMessageProps = {
  setResponse: React.Dispatch<
    React.SetStateAction<
      {
        role: string;
        response: string;
      }[]
    >
  >;
} & UserMessageProps;

function BotMessage<BotMessageProps>({ message, setResponse }) {
  if (message && message.question) {
    return (
      <div
        style={{
          width: "100%",
          display: "flex",
          justifyContent: "flex-start",
          flexWrap: "wrap",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "flex-end",
            gap: "4px",
            flexWrap: "wrap",
          }}
        >
          <div
            style={{
              width: "24px",
              height: "24px",
              borderRadius: "50%",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              background: "#fff",
            }}
          >
            <GoHubot />
          </div>
          <div className="message-wrapper">
            <p>{message.question}</p>
          </div>
        </div>
      </div>
    );
  } else if (message && message.recommendations) {
    return (
      <div style={{ width: "100%", display: "flex" }}>
        <div
          style={{
            display: "flex",
            alignItems: "flex-end",
            gap: "4px",
            flexWrap: "wrap",
          }}
        >
          <div
            style={{
              width: "24px",
              height: "24px",
              borderRadius: "50%",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              background: "#fff",
            }}
          >
            <GoHubot />
          </div>
          <div className="recommendations-wrapper">
            {message.recommendations.map((rec) => (
              <div
                style={{
                  background: `url(${rec.image_link}) no-repeat center center`,
                  backgroundSize: "cover",
                  width: "100px",
                  height: "100px",
                  borderRadius: "6px",
                }}
              >
                <div style={{ display: "flex", flexDirection: "row-reverse" }}>
                  <button
                    style={{
                      backgroundColor: "#C86C53",
                      padding: "4px",
                      borderRadius: "6px",
                    }}
                    onClick={(e) => {
                      e.preventDefault();
                      axios
                        .get(`http://localhost:8000/regenerate-item`, {
                          params: {
                            search_query: rec.search_query,
                          },
                        })
                        .then((res) => {
                          if (res.data) {
                            setResponse((prevResponses) => {
                              return [
                                ...prevResponses,
                                { role: "bot", response: res.data },
                              ];
                            });
                          }
                        });
                    }}
                  >
                    <PiShuffle color="white" />
                  </button>
                </div>
                {/* <p>{rec.product_link}</p> */}
                <div>
                  <p>{rec.product_price}</p>
                  <button>
                    <ShoppingCartIcon sx={{ paddingRight: "0.25rem" }} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }
  return null;
}

const ChatBotWrapper = styled.div`
  min-height: 100vh;
  min-width: 100vw;
  padding: 6rem;
  display: flex;
  justify-content: center;
  .input {
    width: calc(100% / 2);
    bottom: 1rem;
    background: #d9d9d9;
    border-radius: 20px;
    padding: 6px 8px 6px 16px;
    display: flex;
    align-items: center;
    position: fixed;
    input {
      all: unset;
      padding: 0.5rem;
      flex-grow: 1;
    }
    button {
      display: flex;
      gap: 4px;
      border-radius: 16px;
      background: #c86c53;
      color: #fff;
      padding: 12px 12px;
      font-weight: 400;
    }
  }
`;

const ChatList = styled.div`
  width: calc(100% / 2);
  display: flex;
  flex-direction: column;
  gap: 1.5rem;

  .message-wrapper {
    padding: 1rem;
    background-color: #d9d9d9;
    border-radius: 8px;
    p {
      color: #000;
      font-weight: 400;
      flex-wrap: wrap;
    }
  }
  .recommendations-wrapper {
    padding: 1rem;
    background-color: #d9d9d9;
    border-radius: 8px;
    display: flex;
    flex-wrap: "wrap";
  }
`;
