// import NextAuth from "next-auth";
// import CredentialsProvider from "next-auth/providers/credentials";
// import api from "@/utils/api";

// export default NextAuth({
//   providers: [
//     CredentialsProvider({
//       name: "Credentials",
//       async authorize(credentials) {
//         const res = await api.post("/auth/login", credentials);
//         return res.data || null;
//       },
//     }),
//   ],
// });
