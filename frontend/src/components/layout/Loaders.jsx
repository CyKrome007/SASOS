import {Grid, Skeleton, Stack} from "@mui/material";

const LayoutLoader = () => {
    return (
        <>
            <Grid container height={"calc(100vh - 4rem)"} spacing={'1rem'}>
                <Grid item sm={4} md={3} sx={{
                    display: {
                        xs: 'none',
                        sm: 'block'
                    },
                }} height={"100%"} >
                    <Skeleton variant='rounded' height={'100vh'} />
                </Grid>
                <Grid item xs={12} sm={8} md={5} lg={6} height={"100%"} >
                    <Stack spacing={'1rem'}>
                        {
                            Array.from({ length: 10 }).map((_, i) => (
                                <Skeleton key={i} variant='rounded' height={'5rem'}/>
                            ))
                        }
                    </Stack>
                </Grid>
                <Grid item sm={4} md={4} lg={3} height={"100%"} sx={{
                    display: {
                        xs: 'none',
                        sm: 'block'
                    },
                }}>
                    <Skeleton variant='rounded' height={'100vh'} />
                </Grid>
            </Grid>
        </>
    )
}

export default LayoutLoader;
