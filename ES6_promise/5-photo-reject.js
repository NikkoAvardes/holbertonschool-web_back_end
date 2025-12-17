export default function uploadPhoto(filename) {
  const fileName = filename
  return new Promise((resolved, rejected) => {
	rejected(new Error(`${fileName} cannot be uploaded`));
  });
}