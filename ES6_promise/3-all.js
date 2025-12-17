import { uploadPhoto, createUser } from './utils.js'
export default async function handleProfileSignup() {
  const photoPromise = uploadPhoto();
  const userPromise = createUser();
  try {
	const [photo, user] = await Promise.all([photoPromise, userPromise]);
	console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  } catch (error) {
	console.log('Signup system offline');
  }
}