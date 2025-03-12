import Header from "./Header.jsx";
// import Title from "../shared/Title.jsx";
import { Drawer, Skeleton, Grid2 } from "@mui/material";
import { useNavigate, useParams } from "react-router-dom";
import { Profile } from "../specific/Profile.jsx";
import { useDispatch, useSelector } from "react-redux";
import { setIsDeleteMenu, setIsMobile, setSelectedDeleteChat } from "../../redux/reducers/misc.js";
import {useCallback, useEffect, useRef, useState} from "react";
import { getOrSaveFromStorage } from "../../lib/features.js";

const AppLayout = () => (WrappedComponent) => {
    // eslint-disable-next-line react/display-name
    return (props) => {

        // eslint-disable-next-line react-hooks/rules-of-hooks
        const params = useParams();
        // eslint-disable-next-line react-hooks/rules-of-hooks
        const dispatch = useDispatch();
        // eslint-disable-next-line react-hooks/rules-of-hooks
        const navigate = useNavigate();
        // eslint-disable-next-line react-hooks/rules-of-hooks
        const deleteMenuAnchor = useRef(null);

        // eslint-disable-next-line react-hooks/rules-of-hooks
        const [onlineUsers, setOnlineUsers] = useState([]);
        const chatId = params.chatId;


        const { isMobile } = useSelector((state) => state['misc']);

        const { user } = useSelector((state) => state.auth);


        const handleMobileClose = () => dispatch(setIsMobile(false));

        return (
            <>
                {/*<Title />*/}
                <Header />

                {/*{*/}
                {/*    isLoading ? (*/}
                {/*        <Skeleton />*/}
                {/*    ) : (*/}
                {/*        <Drawer open={isMobile} onClose={handleMobileClose}>*/}
                {/*            <ChatList*/}
                {/*                w={'85vw'}*/}
                {/*                chats={data?.chats}*/}
                {/*                chatId={chatId}*/}
                {/*                handleDeleteChat={handleDeleteChat}*/}
                {/*                newMessagesAlert={newMessagesAlert}*/}
                {/*                onlineUsers={onlineUsers}*/}
                {/*            />*/}
                {/*        </Drawer>*/}
                {/*    )*/}
                {/*}*/}

                <Grid2 container height={"calc(100vh - 4rem)"}>
                    <Grid2 size={{ xs: 12 }} height={"100%"} >
                        <WrappedComponent {...props} chatId={chatId} user={user} />
                    </Grid2>
                </Grid2>
            </>
        );
    };

}

export default AppLayout;