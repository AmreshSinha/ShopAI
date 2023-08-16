import React from "react";
import styled from "styled-components";
import axios from "axios";
import { MdPerson } from "react-icons/md";
import { GoHubot } from "react-icons/go";
import { PiPaperPlaneRightFill } from "react-icons/pi";

type ChatBotProps = {
  queryAsked: string;
};

export default function ChatBot<ChatBotProps>({ queryAsked }) {
  const [localQueryAsked, setLocalQueryAsked] = React.useState("");
  const [response, setResponse] = React.useState<
    Array<{ role: string; response: any }>
  >([{ role: "user", response: queryAsked }]);

  return (
    <ChatBotWrapper>
      <ChatList>
        {response?.map((res) =>
          res.role === "user" ? (
            <UserMessage message={res.response} />
          ) : (
            <BotMessage message={res.response} />
          )
        )}
      </ChatList>
      <form
        className="input"
        onSubmit={(e) => {
          e.preventDefault();
          const formData = new FormData(e.currentTarget);
          const data = Object.fromEntries(formData.entries());
          setLocalQueryAsked(data.query as string);
        }}
      >
        <input
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
    <div style={{ width: "100%", display: "flex", justifyContent: "flex-end" }}>
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

function BotMessage<UserMessageProps>({ message }) {
  return (
    <div
      style={{ width: "100%", display: "flex", justifyContent: "flex-start" }}
    >
      <div style={{ display: "flex", alignItems: "flex-end", gap: "4px" }}>
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
          <p>{message}</p>
        </div>
      </div>
    </div>
  );
}

const ChatBotWrapper = styled.div`
  min-height: 100vh;
  min-width: 100vw;
  padding: 6rem;
  display: flex;
  justify-content: center;
  .input {
    width: calc(100%/2);
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
`;
