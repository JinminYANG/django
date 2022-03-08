import TextField from '@mui/material/TextField';
import Checkbox from '@mui/material/Checkbox';
import Button from '@mui/material/Button';
import FormControlLabel from '@mui/material/FormControlLabel';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import {CssBaseline} from "@mui/material";


function SignIn() {
    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        console.log({
            email: data.get('email'),
            password: data.get('password'),
        });
    };

    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign In
                </Typography>
                <Box component="form" onSubmit={handleSubmit}>
                    <TextField
                        label="Email Address"
                        id="email"
                        required
                        fullWidth
                        name="email"
                        autoComplete="email"
                        autoFocus
                        margin="normal"
                    />
                    <TextField
                        label="Password"
                        id="password"
                        type="password"
                        required
                        fullWidth
                        name="password"
                        autoComplete="current-password"
                        margin="normal"
                    />
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Sign in
                    </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link to="/update">Forgot password?</Link>
                        </Grid>
                        <Grid item>
                            <Link>Sign Up</Link>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
        </Container>
    );
}

export default SignIn;

// autoComplete - 모바일에서 이메일을 입력하도록 도와주는 기능
// FormControlLabel - control의 props 값으로 Checkbox를 준다.
// variant - Button의 모양을 결정하는 props
// sx - 컴포넌트의 디자인을 간단하게 고치고 싶을 때 사용
// xs - (auto layout) 여러 개의 구성요소들이 있을 때 xs라고 지정된 그리드가 컬럼의 빈 공간을 차지하게 된다.
// Typography - 텍스트의 폰트를 지정할 수 있도록 해주는 도구 (component="h1" 이 부분이 h1 태그로 감싸지게 될 것이다.) (variant="h5" MUI에서 지정한 h5에 대한 다지인을 적용하겠다.)
// Avatar - 동그란 모양의 ui를 만들 수 있게 도와주는 도구
// Box - html 태그 중에서 div와 같은 역할
// {display: 'flex', flexDirection: 'column'} - 열의 방향으로 컨텐츠를 배치시킨다.
