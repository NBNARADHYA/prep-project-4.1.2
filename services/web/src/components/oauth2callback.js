import { useContext, useEffect } from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import { AccessTokenContext } from '../store/contexts/accessToken.context';

export const Oauth2Callback = () => {
  const { setAccessToken } = useContext(AccessTokenContext);
  const history = useHistory();
  const location = useLocation();

  useEffect(() => {
    let url = `${process.env.REACT_APP_BACKEND_HOST}/oauth/oauth2callback?`;
    url += location.search.substr(1);
    // Add all url params sent by google to backend /oauth2callback url
    // Object.keys(urlParams).forEach((key) => {
    //   url += `${key}=${urlParams[key]}&`
    // })

    fetch(url, { credentials: 'include' })
      .then(async (res) => res.json())
      .then((res) => {
        if (!res.result || !res.access_token) {
          throw new Error();
        }
        setAccessToken(res.access_token);
        history.push('/');
      })
      .catch((err) => console.error(err));
    // eslint-disable-next-line
  }, [location]);

  return null;
};
