import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(
  firstName,
  lastName,
  fileName,
) {
  const promises = [signUpUser(firstName, lastName),
    uploadPhoto(fileName)];

  return Promise.allSettled(promises)
    .then((values) => {
      const arr = [];
      values.forEach((value) => {
        if (value.status === 'fulfilled') {
          arr.push(value);
        } else {
          arr.push({
            status: value.status,
            value: `Error: ${value.reason.message}`,
          });
        }
      });
      return arr;
    });
}
