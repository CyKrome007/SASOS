import {
    AppBar, Avatar, Backdrop, Badge, Box, IconButton, Menu, MenuItem,
    Toolbar, Tooltip, Typography
} from "@mui/material";

import {
    Menu as MenuIcon,
    Logout as LogoutIcon,
    Person as PersonIcon,
} from "@mui/icons-material";


import { useNavigate } from "react-router-dom";
import {lazy, Suspense, useEffect, useState} from "react";
import axios from "axios";
import { server } from "../../constants/config.js";
import toast from "react-hot-toast";
import { useDispatch, useSelector } from "react-redux";
import { userNotExists } from "../../redux/reducers/auth.js";
import { setIsMobile } from "../../redux/reducers/misc.js";

// const SearchDialogue = lazy(() => import("../specific/Search.jsx"));
// const NotificationsDialogue = lazy(() => import("../specific/Notifications.jsx"));
// const NewGroupDialogue = lazy(() => import("../specific/NewGroup.jsx"));


const Header = () => {

    const navigate = useNavigate();
    const dispatch = useDispatch();

    const { isSearch, isNotification, isNewGroup } = useSelector((state) => state['misc']);
    const { user } = useSelector((state) => state['auth']);
    // const { notificationCount } = useSelector((state) => state.chat);

    const [anchorElUser, setAnchorElUser] = useState(null);
    const [avatar, setAvatar] = useState('')

    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    const handleMobile = (e) => {
        e.preventDefault();
        dispatch(setIsMobile(true));
    }

    const openProfile = (e) => {
        e.preventDefault();
        handleCloseUserMenu();
        navigate('/profile');
    }

    const handleLogout = async () => {
        try{
            const {data} = await axios.get(
                `${server}/user/logout`, {
                    withCredentials: true,
                }
            );
            toast.success(data?.message || 'Logout Success');
            dispatch(userNotExists());
        } catch (e) {
            toast.error(e?.response?.data?.message || 'Something Went Wrong');
        }
    }

    useEffect(() => {setAvatar(user?.avatar?.url)}, [user])


    return (
        <>
            <Box
                sx={{
                    flexGrow: 1,
                }}
                height="4rem"
            >
                <AppBar
                    position="static"
                    sx={{
                        bgcolor: 'white',
                    }}
                >
                    <Toolbar>
                        <Box
                            display="flex"
                            flexDirection="row"
                        >
                            <Typography
                                variant='h5'
                                display={'block'}
                                fontWeight={700}
                                color={'#C4D630'}
                            >
                                Krishi&nbsp;
                            </Typography>
                            <Typography
                                variant='h5'
                                display={'block'}
                                fontWeight={700}
                                color={'#00A550'}
                            >
                                Khet&nbsp;
                            </Typography>
                            <Typography
                                variant='h5'
                                display={'block'}
                                fontWeight={700}
                                color={'#C4D630'}
                            >
                                Exchange
                            </Typography>

                        </Box>
                        <Box
                            sx={{
                                display: {
                                    xs: 'block',
                                    sm: 'none',

                                },
                                bgcolor: '#00A550',
                                paddingRight: '1rem'
                            }}
                        >
                            <IconButton color='inherit' onClick={handleMobile}>
                                <MenuIcon />
                            </IconButton>
                        </Box>
                        <Box
                            sx={{
                                flexGrow: 1,
                                bgcolor: '#00A550'
                            }}
                        />
                        {/*<Box sx={{*/}
                        {/*    display: {*/}
                        {/*        xs: 'none',*/}
                        {/*        md: 'block'*/}
                        {/*    }*/}
                        {/*}}>*/}
                        {/*    /!*<IconBtn title={'Search'} icon={<SearchIcon />} onClick={openSearch} />*!/*/}
                        {/*    /!*<IconBtn title={'New Group'} icon={<AddIcon />} onClick={openNewGroup} />*!/*/}
                        {/*    /!*<IconBtn title={'Manage Groups'} icon={<GroupIcon />} onClick={navigateToGroups} />*!/*/}
                        {/*    /!*<IconBtn title={'Notifications'} icon={<NotificationsIcon />} value={notificationCount} onClick={openNotification} />*!/*/}
                        {/*    <IconBtn title={'Profile'} icon={<PersonIcon sx={{color: 'black'}} />} onClick={openProfile} />*/}
                        {/*    <IconBtn title={'Logout'} icon={<LogoutIcon sx={{color: 'black'}}/>} onClick={handleLogout} />*/}
                        {/*</Box>*/}
                        <Box sx={{
                            display: {
                                xs: 'block',
                                md: 'block'
                            }
                        }}>
                            <Box sx={{ flexGrow: 0 }}>
                                <Tooltip title="Open settings">
                                    <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                                        <Avatar alt={user?.name} src={avatar}/>
                                    </IconButton>
                                </Tooltip>
                                <Menu
                                    sx={{ mt: '45px' }}
                                    id="menu-appbar"
                                    anchorEl={anchorElUser}
                                    anchorOrigin={{
                                        vertical: 'top',
                                        horizontal: 'right',
                                    }}
                                    keepMounted
                                    transformOrigin={{
                                        vertical: 'top',
                                        horizontal: 'right',
                                    }}
                                    open={Boolean(anchorElUser)}
                                    onClose={handleCloseUserMenu}
                                >
                                    {/*settings.map((setting) => (
                                        <MenuItem key={setting} onClick={handleCloseUserMenu}>
                                            <Typography sx={{ textAlign: 'center' }}>{setting}</Typography>
                                        </MenuItem>
                                    ))*/}
                                    {/*<MenuItem onClick={openSearch}>*/}
                                    {/*    <IconBtn title={'Search'} icon={<SearchIcon />} />*/}
                                    {/*    <Typography variant='body1' sx={{ paddingRight: '1rem'}}>Search Users</Typography>*/}
                                    {/*</MenuItem>*/}
                                    {/*<MenuItem onClick={openNewGroup}>*/}
                                    {/*    <IconBtn title={'New Group'} icon={<AddIcon />} />*/}
                                    {/*    <Typography variant='body1' sx={{ paddingRight: '1rem'}}>New Group</Typography>*/}
                                    {/*</MenuItem>*/}
                                    {/*<MenuItem onClick={navigateToGroups}>*/}
                                    {/*    <IconBtn title={'Manage Groups'} icon={<GroupIcon />} />*/}
                                    {/*    <Typography variant='body1' sx={{ paddingRight: '1rem'}}>Manage Groups</Typography>*/}
                                    {/*</MenuItem>*/}
                                    {/*<MenuItem onClick={openNotification}>*/}
                                    {/*    <IconBtn title={'Notifications'} icon={<NotificationsIcon />} value={notificationCount} />*/}
                                    {/*    <Typography variant='body1' sx={{ paddingRight: '1rem'}}>Notifications</Typography>*/}
                                    {/*</MenuItem>*/}
                                    <MenuItem onClick={openProfile}>
                                        <IconBtn title={'Profile'} icon={<PersonIcon />} />
                                        <Typography variant='body1' sx={{ paddingRight: '1rem'}}>Profile</Typography>
                                    </MenuItem>
                                    <MenuItem onClick={handleLogout}>
                                        <IconBtn title={'Logout'} icon={<LogoutIcon />} />
                                        <Typography variant='body1' sx={{ paddingRight: '1rem'}}>Logout</Typography>
                                    </MenuItem>
                                </Menu>
                            </Box>
                        </Box>
                    </Toolbar>
                </AppBar>
            </Box>
        </>
    )
}

// @ts-ignore
const IconBtn = ({title, icon, onClick, value}) => {
    return(
        <>
            <Tooltip title={title}>
                <IconButton color='inherit' size='large' onClick={onClick}>
                    {
                        value ? (
                            <Badge badgeContent={value} color='error'>{icon}</Badge>
                        ) : (
                            icon
                        )
                    }
                </IconButton>
            </Tooltip>
        </>
    )
}

export default Header;