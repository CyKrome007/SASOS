import AppLayout from "../components/layout/AppLayout.jsx";
import { Box, Button, Container, Grid, Typography, Card, CardContent, CardMedia } from "@mui/material";
import { styled } from "@mui/material/styles";
import AgricultureIcon from '@mui/icons-material/Agriculture';
import MonetizationOnIcon from '@mui/icons-material/MonetizationOn';
import GroupsIcon from '@mui/icons-material/Groups';
import HandshakeIcon from '@mui/icons-material/Handshake';
import {Button as FindOutMoreButton} from '../components/shared/Button.jsx';

const HeroSection = styled(Box)(({ theme }) => ({
  // background: 'linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("public/Background.png")',
  background: 'url("public/Background.png")',
  backgroundSize: 'cover',
  backgroundPosition: 'center',
  color: 'white',
  padding: theme.spacing(15, 0),
  textAlign: 'center',
}));

const FeatureCard = styled(Card)(({ theme }) => ({
  background: 'url("public/Background.png")',
  backgroundSize: 'cover',
  backgroundPosition: 'center',
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  padding: theme.spacing(3),
  transition: 'transform 0.3s ease-in-out',
  '&:hover': {
    transform: 'translateY(-10px)',
  },
}));

const features = [
  {
    icon: <AgricultureIcon sx={{ fontSize: 50, color: '#4CAF50' }} />,
    title: 'Smart Farming',
    description: 'Implement modern farming techniques and technologies for better yield.',
  },
  {
    icon: <MonetizationOnIcon sx={{ fontSize: 50, color: '#4CAF50' }} />,
    title: 'Fair Pricing',
    description: 'Get the best market prices for your agricultural products.',
  },
  {
    icon: <GroupsIcon sx={{ fontSize: 50, color: '#4CAF50' }} />,
    title: 'Community Support',
    description: 'Connect with other farmers and share knowledge and resources.',
  },
  {
    icon: <HandshakeIcon sx={{ fontSize: 50, color: '#4CAF50' }} />,
    title: 'Direct Trading',
    description: 'Trade directly with buyers without intermediaries.',
  },
];

const Home = () => {

  return (
    <>
      <HeroSection>
        <Container>
          <Typography variant="h2" component="h1" gutterBottom direction="row" sx={{ color: 'black', mb: 4, fontWeight: 700, fontSize: '4rem', lineHeight: '1.25' }}>
            Welcome to
          </Typography>
            <Typography
                variant='h2'
                display={'block'}
                fontWeight={700}
                color={'#C4D630'}
            >
                Krishi&nbsp;
            </Typography>
            <Typography
                variant='h2'
                display={'block'}
                fontWeight={700}
                color={'#00A550'}
            >
                Khet&nbsp;
            </Typography>
            <Typography
                variant='h2'
                display={'block'}
                fontWeight={700}
                color={'#C4D630'}
            >
                Exchange
            </Typography>
          <Typography variant="h5" component="h2" sx={{ mb: 4 }}>
            Where Landowners and Cultivators Thrive
          </Typography>
          {/*<Button*/}
          {/*  variant="contained"*/}
          {/*  size="large"*/}
          {/*  sx={{*/}
          {/*    backgroundColor: '#4CAF50',*/}
          {/*    '&:hover': { backgroundColor: '#45a049' },*/}
          {/*  }}*/}
          {/*>*/}
          {/*  Get Started*/}
          {/*</Button>*/}
          <FindOutMoreButton content={'Get Started'} />
        </Container>
      </HeroSection>

      <Container sx={{ py: 8 }}>
        <Typography variant="h3" component="h2" textAlign="center" gutterBottom>
          Our Features
        </Typography>
        <Typography variant="h6" component="p" textAlign="center" color="text.secondary" sx={{ mb: 6 }}>
          Discover how we can help you grow your farming business
        </Typography>

        <Grid container spacing={4}>
          {features.map((feature, index) => (
            <Grid item xs={12} sm={6} md={3} key={index}>
              <FeatureCard>
                {feature.icon}
                <CardContent>
                  <Typography variant="h5" component="h3" gutterBottom textAlign="center">
                    {feature.title}
                  </Typography>
                  <Typography color="text.secondary" textAlign="center">
                    {feature.description}
                  </Typography>
                </CardContent>
              </FeatureCard>
            </Grid>
          ))}
        </Grid>
      </Container>

      <Box sx={{ bgcolor: '#f5f5f5', py: 8 }}>
        <Container>
          <Grid container spacing={4} alignItems="center">
            <Grid item xs={12} md={6}>
              <Typography variant="h3" component="h2" gutterBottom>
                About Our Platform
              </Typography>
              <Typography variant="body1" paragraph>
                SASOS is a comprehensive platform designed to revolutionize the agricultural sector. We provide farmers with the tools and resources they need to succeed in modern agriculture.
              </Typography>
              <Typography variant="body1" paragraph>
                Our platform facilitates direct connections between farmers and buyers, ensuring fair prices and sustainable farming practices.
              </Typography>
              <Button
                variant="contained"
                size="large"
                sx={{
                  backgroundColor: '#4CAF50',
                  '&:hover': { backgroundColor: '#45a049' },
                  mt: 2,
                }}
              >
                Learn More
              </Button>
            </Grid>
            <Grid item xs={12} md={6}>
              <Box
                component="img"
                src="/public/Subscribe.png"
                alt="Farming"
                sx={{
                  width: '100%',
                  borderRadius: 2,
                  boxShadow: 3,
                }}
              />
            </Grid>
          </Grid>
        </Container>
      </Box>
    </>
  );
};

export default AppLayout()(Home);
